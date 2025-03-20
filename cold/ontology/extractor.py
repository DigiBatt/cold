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


from ..utils.helpers import extract_label

def extract_properties(cls, visited=None):
    """Extract properties of a class, ensuring no infinite recursion."""
    if visited is None:
        visited = set()  # Initialize visited set to prevent infinite loops
        
    properties = []
    dependencies = []  # Collect classes mentioned in the range for imports

    # Add fixed `class_iri` and `class_name` properties
    iri_value = getattr(cls, "iri", None)
    if iri_value:
        properties.append({
            "name": "class_iri",
            "range": "str",
            "default": repr(iri_value),  # Use repr to preserve string formatting
        })

    # Extract and convert the prefLabel to a plain string
    name_value = getattr(cls, "prefLabel", [None])[0]
    if name_value:
        plain_name = extract_label(name_value)  # Convert locstr to plain string
        properties.append({
            "name": "class_name",
            "range": "str",
            "default": repr(plain_name),  # Use plain string here
        })

    for prop in cls.get_class_properties():
        try:
            # Skip properties without a prefLabel
            if not hasattr(prop, "prefLabel") or not prop.prefLabel or not prop.prefLabel[0]:
                continue

            # Extract and sanitize the property name
            raw_pref_label = prop.prefLabel[0]
            sanitized_name = sanitize_module_name(extract_label(raw_pref_label))
            sanitized_range = "str"  # Default range to 'str'

            # Access the class-specific property using the sanitized name
            class_prop = getattr(cls, sanitized_name, None)

            if class_prop:
                # Handle restrictions or literals
                if hasattr(class_prop[0], "prefLabel") and class_prop[0].prefLabel:
                    # If the property has a prefLabel, use it
                    range_label = class_prop[0].prefLabel[0]
                    sanitized_range = sanitize_module_name(extract_label(range_label))
                    dependencies.append(f"{sanitized_range}Module")
                elif hasattr(class_prop[0], "value"):
                    # If the property is a literal, use the value
                    sanitized_range = str(class_prop[0].value)
                else:
                    # Default to 'str' if no prefLabel or literal is found
                    sanitized_range = "str"

            # Append the property with its resolved range
            properties.append({
                "name": sanitized_name,
                "range": sanitized_range,
            })

        except Exception as e:
            print(f"Error processing property '{getattr(prop, 'prefLabel', ['Unknown'])[0]}': {e}")
            continue


    return properties, list(set(dependencies))  # Return unique dependencies



def get_parent_classes(cls):
    """Retrieve the parent classes of a given class."""
    parent_classes = []
    if cls.is_a:
        for parent in cls.is_a:
            if hasattr(parent, "prefLabel") and parent.prefLabel:
                parent_classes.append(extract_label(parent.prefLabel[0]))

    return parent_classes if parent_classes else ["LinkedDataModel"]  # Default to BaseModel