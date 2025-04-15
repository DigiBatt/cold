from pydantic import BaseModel, Field, ValidationError
from typing import Optional, List, Union
from urllib.parse import urlparse

# Hardcoded for now, can later extract from TTL context
NAMESPACE_PREFIXES = {
    "https://schema.org/": "schema",
    "https://w3id.org/emmo": "",  # Default — use plain field name
}

class LinkedDataModel(BaseModel):
    class_name: Optional[Union[str, List[str]]] = Field(None)
    class_iri: Optional[str] = Field(None)
    identifier: Optional[str] = Field(None, alias="@id")
    label: Optional[str] = Field(None, alias="rdfs:label")
    comment: Optional[Union[str, List[str]]] = Field(None, alias="rdfs:comment")
    hasProperty: Optional[List[BaseModel]] = Field(default_factory=list)

    class Config:
        populate_by_name = True
        extra = "allow"

    def __setattr__(self, name, value):
        try:
            super().__setattr__(name, value)
        except ValidationError as e:
            seen_errors = set()
            print(f"\nValidation Error assigning '{name}' with value '{value}':")
            for err in e.errors():
                loc_short = " → ".join(str(item) for item in err["loc"][:2])
                if loc_short not in seen_errors:
                    seen_errors.add(loc_short)
                    print(f" - At '{loc_short}': {err['msg']}\n")

    def _get_prefixed_name(self, field_name: str) -> str:
        model_field = self.__fields__.get(field_name)

        if model_field:
            iri = None
            if hasattr(model_field, "json_schema_extra") and model_field.json_schema_extra:
                iri = model_field.json_schema_extra.get("iri")

            # 1. Handle internal EMMO properties
            if iri and "https://w3id.org/emmo" in iri:
                # fallback to clean field_name
                return field_name

            # 2. Handle known namespace properties (schema.org etc.)
            if iri:
                for namespace, prefix in NAMESPACE_PREFIXES.items():
                    if iri.startswith(namespace):
                        suffix = iri.replace(namespace, "")
                        return f"{prefix}:{suffix}" if prefix else suffix

        # 3. Fallback: use field name as is
        return field_name


    def to_jsonld(self, include_context=True) -> dict:
        """Custom JSON-LD serialization method with namespace-aware keys."""
        jsonld_data = {}

        if include_context:
            jsonld_data["@context"] = "https://w3id.org/emmo/domain/battery/context"

        if self.class_name:
            jsonld_data["@type"] = self.class_name

        # Combine standard and extra fields
        all_fields = {**self.__dict__, **getattr(self, '__pydantic_extra__', {})}

        for field_name, value in all_fields.items():
            if field_name in {"class_iri", "class_name"} or value in [None, []]:
                continue

            key = self._get_prefixed_name(field_name)

            # Handle nested LinkedDataModel(s)
            if isinstance(value, LinkedDataModel):
                jsonld_data[key] = value.to_jsonld(include_context=False)
            elif isinstance(value, list):
                nested = [
                    v.to_jsonld(include_context=False) if isinstance(v, LinkedDataModel) else v
                    for v in value if v is not None
                ]
                if nested:
                    jsonld_data[key] = nested
            else:
                jsonld_data[key] = value

        return jsonld_data
