def extract_label(value):
    """
    Extract a label from a class or literal-like object.
    Falls back to the IRI fragment if no label is available.
    """
    try:
        # If it's a full ontology entity (class or property)
        if hasattr(value, "prefLabel") and value.prefLabel:
            return str(value.prefLabel[0])
        elif hasattr(value, "label") and value.label:
            return str(value.label[0])
        elif hasattr(value, "name"):
            return str(value.name)
        elif hasattr(value, "iri"):
            return value.iri.split("#")[-1].split("/")[-1]
        elif hasattr(value, "value"):
            return str(value.value)  # owlready2 locstr
        elif isinstance(value, dict) and "@value" in value:
            return value["@value"]
        return str(value)
    except Exception:
        return "UnnamedClass"



def get_prefLabel(cls, else_):
    if hasattr(cls, "prefLabel") and cls.prefLabel:
        return extract_label(cls.prefLabel[0])
    elif hasattr(cls, "label") and cls.label:
        return extract_label(cls.label[0])
    elif hasattr(cls, "get_preferred_label") and cls.get_preferred_label() is not None:
        return extract_label(cls.get_preferred_label())
    else:
        return else_


from pydantic import create_model, BaseModel
from typing import Type, List, Optional, Any

def merge_models(*models: Type[BaseModel], class_name: Optional[str] = None) -> Type[BaseModel]:
    """
    Dynamically creates a new Pydantic model that merges multiple base models.

    :param models: Base Pydantic model classes to merge.
    :param class_name: Optional custom class name. If None, it's auto-generated.
    :return: A new dynamically generated Pydantic model class.
    """
    if not models:
        raise ValueError("At least one model is required.")

    fields = {}

    # Collect all fields from base models
    for model in models:
        for name, field in model.__annotations__.items():
            fields[name] = (field, None)  # Default to None if not required

    # Auto-generate class_name by concatenating constituent model class_names
    class_names = [cls.__name__ for cls in models]
    auto_class_name = "".join(class_names)

    # Ensure class_name is a merged list
    combined_class_names = list(set(getattr(cls, "class_name", cls.__name__) for cls in models))
    fields["class_name"] = (List[str], combined_class_names)

    # Ensure class_iri is selected properly (use first non-null value)
    class_iris = [getattr(model, "class_iri", None) for model in models if getattr(model, "class_iri", None)]
    fields["class_iri"] = (Optional[str], class_iris[0] if class_iris else None)

    # Use the auto-generated name if no custom class_name is provided
    return create_model(class_name or auto_class_name, **fields, __base__=models)

import uuid

def assign_ids(jsonld, base_iri="https://zenodo.org/record/123456789#"):
    """
    Recursively assigns a unique @id to each object node in a JSON-LD graph
    if it doesn't already have one.

    Args:
        jsonld (dict): The JSON-LD document.
        base_iri (str): The base IRI to prefix each generated ID (should end with '#').

    Returns:
        dict: The updated JSON-LD document with @id fields.
    """

    def process_node(node):
        if isinstance(node, dict):
            if "@type" in node and "@id" not in node:
                node["@id"] = f"{base_iri}uuid-{uuid.uuid4()}"
            for key, value in node.items():
                node[key] = process_node(value)
        elif isinstance(node, list):
            return [process_node(item) for item in node]
        return node

    return process_node(jsonld)
