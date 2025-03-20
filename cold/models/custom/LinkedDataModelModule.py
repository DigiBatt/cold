from pydantic import BaseModel, Field, ValidationError
from typing import Optional, List, Union

class LinkedDataModel(BaseModel):
    class_name: Optional[Union[str, List[str]]] = Field(None)
    class_iri: Optional[str] = Field(None)
    identifier: Optional[str] = Field(None, alias="@id")
    label: Optional[str] = Field(None, alias="rdfs:label")
    comment: Optional[Union[str, List[str]]] = Field(None, alias="rdfs:comment")
    hasProperty: Optional[List[BaseModel]] = Field(default_factory=list)

    class Config:
        populate_by_name = True  # Enable alias population during instantiation
        extra = "allow"  # <--- Explicitly allow arbitrary properties here


    def __setattr__(self, name, value):
        try:
            super().__setattr__(name, value)
        except ValidationError as e:
            seen_errors = set()
            print(f"\nValidation Error assigning '{name}' with value '{value}':")
            for err in e.errors():
                # Extract just the first two parts of the loc path to remove redundancy
                loc_short = " → ".join(str(item) for item in err["loc"][:2])
                if loc_short not in seen_errors:
                    seen_errors.add(loc_short)
                    print(f" - At '{loc_short}': {err['msg']}\n")

    def to_jsonld(self, include_context=True) -> dict:
        """Custom JSON-LD serialization method, explicitly handling extra fields."""
        jsonld_data = {}

        # Add context only at the top level
        if include_context:
            jsonld_data["@context"] = "https://w3id.org/emmo/domain/battery/context"

        # Add @type for class_name if it exists
        if self.class_name:
            jsonld_data["@type"] = self.class_name

        # Combine explicitly defined fields and extra fields
        all_fields = {**self.__dict__, **getattr(self, '__pydantic_extra__', {})}

        # Process all fields, explicitly excluding unwanted ones
        for field_name, value in all_fields.items():
            if field_name in {"class_iri", "class_name"} or value is None or value == []:
                continue  # Skip unwanted fields and empty values

            # Serialize nested LinkedDataModel instances
            if isinstance(value, LinkedDataModel):
                nested_jsonld = value.to_jsonld(include_context=False)
                if nested_jsonld:
                    jsonld_data[field_name] = nested_jsonld
            elif isinstance(value, list):
                # Serialize lists, recursively serializing nested LinkedDataModels
                nested_list = [
                    v.to_jsonld(include_context=False) if isinstance(v, LinkedDataModel) else v
                    for v in value if v is not None
                ]
                if nested_list:
                    jsonld_data[field_name] = nested_list
            else:
                # Add scalar fields
                jsonld_data[field_name] = value

        return jsonld_data


