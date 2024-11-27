from pydantic import BaseModel, Field
from typing import Optional, List, Union

class LinkedDataModel(BaseModel):
    class_name: Optional[Union[str, List[str]]] = Field(None)
    class_iri: Optional[str] = Field(None)
    identifier: Optional[str] = Field(None, alias="@id")
    label: Optional[str] = Field(None, alias="rdfs:label")
    comment: Optional[Union[str, List[str]]] = Field(None, alias="rdfs:comment")
    hasProperty: Optional[List[BaseModel]] = Field(default_factory=list)

    class Config:
        populate_by_name = True


    class Config:
        populate_by_name = True  # Enable alias population during instantiation

    def to_jsonld(self, include_context=True) -> dict:
        """Custom JSON-LD serialization method."""
        jsonld_data = {}

        # Add context only at the top level
        if include_context:
            jsonld_data["@context"] = "https://w3id.org/emmo/domain/battery/context"

        # Add @type for class_name if it exists
        if self.class_name:
            jsonld_data["@type"] = self.class_name

        # Process fields and exclude `class_iri`, `class_name`, and empty values
        for field_name, value in self.__dict__.items():
            if field_name in {"class_iri", "class_name"} or value is None or value == []:
                continue  # Skip class_iri, class_name, None, and empty lists

            # Serialize nested LinkedDataModel instances
            if isinstance(value, LinkedDataModel):
                nested_jsonld = value.to_jsonld(include_context=False)
                if nested_jsonld:  # Ensure the nested object is not empty
                    jsonld_data[field_name] = nested_jsonld
            elif isinstance(value, list):
                # Serialize lists of LinkedDataModel or other objects, excluding empty lists
                nested_list = [
                    v.to_jsonld(include_context=False) if isinstance(v, LinkedDataModel) else v
                    for v in value if v is not None
                ]
                if nested_list:  # Add only non-empty lists
                    jsonld_data[field_name] = nested_list
            else:
                # Add scalar fields
                jsonld_data[field_name] = value

        return jsonld_data

