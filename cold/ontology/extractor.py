from cold.utils.sanitizers import sanitize_module_name
from cold.utils.helpers import extract_label

def extract_classes(ontology, allowed_classes=None, max_classes=None):
    """Extract classes from the ontology."""
    ontology_classes = []

    if allowed_classes is None:
        print("No allowed_classes specified. Extracting all classes from the ontology...")
        for cls in ontology.classes():
            class_name = cls.prefLabel[0] if hasattr(cls, "prefLabel") and cls.prefLabel else ""
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

from owlready2 import Restriction
from ..utils.helpers import extract_label
from cold.utils.sanitizers import sanitize_module_name

def extract_properties(cls, visited=None):
    if visited is None:
        visited = set()

    properties = []
    dependencies = []
    seen_property_names = set()

    # Add fixed metadata
    iri_value = getattr(cls, "iri", None)
    if iri_value:
        properties.append({
            "name": "class_iri",
            "range": "str",
            "default": repr(iri_value),
            "iri": str(iri_value)
        })
        seen_property_names.add("class_iri")

    name_value = getattr(cls, "prefLabel", [None])[0]
    if name_value:
        plain_name = extract_label(name_value)
        properties.append({
            "name": "class_name",
            "range": "str",
            "default": repr(plain_name),
            "iri": None
        })
        seen_property_names.add("class_name")

    # --- Handle owl:Restrictions (EMMO + schema.org) ---
    for parent in cls.is_a:
        if hasattr(parent, "property") and (hasattr(parent, "some_values_from") or hasattr(parent, "all_values_from")):
            try:
                prop = parent.property
                prop_name = sanitize_module_name(getattr(prop, "name", "unknown_property"))
                if prop_name in seen_property_names:
                    continue

                range_type = "str"
                range_cls = parent.some_values_from or parent.all_values_from
                range_iri = getattr(range_cls, "iri", None)

                if range_cls:
                    if hasattr(range_cls, "prefLabel") and range_cls.prefLabel:
                        range_type = sanitize_module_name(extract_label(range_cls.prefLabel[0]))
                        dependencies.append(f"{range_type}Module")
                    elif hasattr(range_cls, "name"):
                        range_type = sanitize_module_name(range_cls.name)
                    elif range_iri:
                        range_type = sanitize_module_name(range_iri.split("/")[-1])

                properties.append({
                    "name": prop_name,
                    "range": range_type,
                    "iri": str(getattr(prop, "iri", ""))
                })
                seen_property_names.add(prop_name)

            except Exception as e:
                print(f"Warning: failed to process restriction in class '{cls.name}': {e}")
                continue

    # --- Handle normal class properties (EMMO-style) ---
    for prop in cls.get_class_properties():
        try:
            if not hasattr(prop, "prefLabel") or not prop.prefLabel or not prop.prefLabel[0]:
                continue

            raw_pref_label = prop.prefLabel[0]
            sanitized_name = sanitize_module_name(extract_label(raw_pref_label))
            if sanitized_name in seen_property_names:
                continue

            sanitized_range = "str"
            class_prop = getattr(cls, sanitized_name, None)

            if class_prop:
                if hasattr(class_prop[0], "prefLabel") and class_prop[0].prefLabel:
                    range_label = class_prop[0].prefLabel[0]
                    sanitized_range = sanitize_module_name(extract_label(range_label))
                    dependencies.append(f"{sanitized_range}Module")
                elif hasattr(class_prop[0], "value"):
                    sanitized_range = str(class_prop[0].value)

            properties.append({
                "name": sanitized_name,
                "range": sanitized_range,
                "iri": str(getattr(prop, "iri", ""))
            })
            seen_property_names.add(sanitized_name)

        except Exception as e:
            print(f"Error processing property '{getattr(prop, 'prefLabel', ['Unknown'])[0]}': {e}")
            continue

    return properties, list(set(dependencies))




def get_parent_classes(cls):
    """Retrieve the parent classes of a given class."""
    parent_classes = []
    if cls.is_a:
        for parent in cls.is_a:
            if hasattr(parent, "prefLabel") and parent.prefLabel:
                parent_classes.append(extract_label(parent.prefLabel[0]))

    return parent_classes if parent_classes else ["LinkedDataModel"]  # Default to BaseModel