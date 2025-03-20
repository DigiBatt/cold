def extract_label(value):
    """
    Extract the plain string from a prefLabel or locstr object.

    Args:
        value: The value to process, which could be a locstr or a plain string.

    Returns:
        str: The plain string representation.
    """
    # Check for the '@value' attribute or similar
    if hasattr(value, 'value'):
        return getattr(value, 'value')  # Access the 'value' attribute directly
    # If it's a locstr with dictionary-like behavior
    if isinstance(value, dict) and '@value' in value:
        return value['@value']
    # Otherwise, return the string representation
    return str(value)


def get_prefLabel(cls, else_):
    if hasattr(cls, "prefLabel") and cls.prefLabel:
        label = cls.prefLabel[0]
    elif hasattr(cls, "get_preferred_label") and cls.get_preferred_label != None:
        label = cls.get_preferred_label()
    else:
        label = else_
    return label

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