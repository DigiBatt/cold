from cold.utils.sanitizers import sanitize_module_name
from cold.utils.helpers import extract_label, get_prefLabel


from rdflib import RDF, RDFS, OWL


def extract_classes(ontology, allowed_classes=None, max_classes=None):
    """Extract classes from the ontology."""
    ontology_classes = []

    if allowed_classes is None:
        print("No allowed_classes specified. Extracting all classes from the ontology...")

        for cls in ontology.classes():

            class_name = get_prefLabel(cls, "")
            # Skip classes starting with a number
            if class_name and class_name[0].isdigit():
                print(f"Skipping class '{class_name}' because it starts with a number.")
                continue
            ontology_classes.append(cls)

    else:
        for class_name in allowed_classes:
            # Skip classes starting with a number
            if class_name[0].isdigit():
                print(f"Skipping class '{class_name}' because it starts with a number.")
                continue

            if hasattr(ontology, class_name):
                ontology_classes.append(getattr(ontology, class_name))
            else:
                print(f"Warning: Class '{class_name}' not found in the ontology.")

    # Apply max_classes limit if specified
    if max_classes:
        return ontology_classes[:max_classes]
    return ontology_classes


from ..utils.helpers import extract_label


def extract_properties(cls):
    """Extract properties of a class."""
    properties = []
    dependencies = []  # Collect classes mentioned in the range for imports

    # Add fixed `class_iri` and `class_name` properties
    iri_value = getattr(cls, "iri", None)
    if iri_value:
        properties.append(
            {
                "name": "class_iri",
                "range": "str",
                "default": repr(iri_value),  # Use repr to preserve string formatting
            }
        )

    # Extract and convert the prefLabel to a plain string
    name_value = get_prefLabel(cls, None)

    # name_value = getattr(cls, "prefLabel", [None])[0]
    if name_value:
        plain_name = extract_label(name_value)  # Convert locstr to plain string

        properties.append(
            {
                "name": "class_name",
                "range": "str",
                "default": repr(plain_name),  # Use plain string here
            }
        )

    for prop in cls.get_class_properties():
        try:

            # if not prop.prefLabel or not prop.prefLabel[0]:
            #     if not prop.get_preferred_label:
            #         continue

            # Extract and sanitize the property name
            raw_pref_label = get_prefLabel(prop, "")

            sanitized_name = sanitize_module_name(extract_label(raw_pref_label))
            sanitized_range = "str"  # Default range to str
            if prop.range and isinstance(prop.range, (list, tuple)) and len(prop.range) > 0:
                range_item = prop.range[0]
                range_value = get_prefLabel(range_item, None) if range_item else None
                # range_value = getattr(range_item, "prefLabel", [None])[0] if range_item else None
                if range_value:
                    sanitized_range = sanitize_module_name(extract_label(range_value))
                    # Add to dependencies with the Module suffix
                    dependencies.append(f"{sanitized_range}Module")

            properties.append(
                {
                    "name": sanitized_name,
                    "range": sanitized_range,
                }
            )
        except Exception as e:
            print(f"Error processing property '{getattr(prop, 'prefLabel', ['Unknown'])[0]}': {e}")
            continue

    return properties, list(set(dependencies))  # Return unique dependencies


def get_parent_classes(cls):
    """Retrieve the parent classes of a given class."""
    parent_classes = []
    if cls.is_a:
        for parent in cls.is_a:
            label = get_prefLabel(parent, None)
            if label:
                parent_classes.append(extract_label(label))

    return parent_classes if parent_classes else ["LinkedDataModel"]  # Default to BaseModel
