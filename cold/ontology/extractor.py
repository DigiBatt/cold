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

import os
from owlready2 import Restriction, ThingClass
from rdflib.term import URIRef
from cold.utils.helpers import extract_label
from cold.utils.sanitizers import sanitize_module_name

DEBUG_LOG_PATH = os.path.join(os.getcwd(), "property_extraction_debug.txt")

def log_debug(message):
    with open(DEBUG_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{message}\n")


def extract_properties(cls, visited=None):
    if visited is None:
        visited = set()

    properties = []
    dependencies = []
    seen_property_names = set()

    log_debug(f"\n--- Extracting properties for class: {getattr(cls, 'name', repr(cls))} ---")

    # Metadata
    iri_value = getattr(cls, "iri", None)
    if iri_value:
        properties.append({
            "name": "class_iri",
            "range": "str",
            "default": repr(iri_value),
            "iri": str(iri_value)
        })
        seen_property_names.add("class_iri")
        log_debug(f"✔ Added class_iri: {iri_value}")

    class_label = extract_label(cls)
    if class_label:
        properties.append({
            "name": "class_name",
            "range": "str",
            "default": repr(class_label),
            "iri": None
        })
        seen_property_names.add("class_name")
        log_debug(f"✔ Added class_name: {class_label}")

    # --- Handle owl:Restrictions (EMMO + schema.org) ---
    for parent in cls.is_a:
        if isinstance(parent, Restriction) and (hasattr(parent, "some_values_from") or hasattr(parent, "all_values_from")):
            try:
                prop = parent.property
                prop_name = sanitize_module_name(getattr(prop, "name", "unknown_property"))
                if prop_name in seen_property_names:
                    continue

                range_cls = parent.some_values_from or parent.all_values_from
                range_type = "str"
                range_info = "unknown"

                if range_cls:
                    if hasattr(range_cls, "prefLabel") and range_cls.prefLabel:
                        range_type = sanitize_module_name(extract_label(range_cls.prefLabel[0]))
                        dependencies.append(f"{range_type}Module")
                        range_info = f"prefLabel: {range_cls.prefLabel[0]}"
                    elif hasattr(range_cls, "name") and range_cls.name:
                        range_type = sanitize_module_name(range_cls.name)
                        dependencies.append(f"{range_type}Module")
                        range_info = f"name: {range_cls.name}"
                    elif hasattr(range_cls, "iri"):
                        iri_str = str(range_cls.iri)
                        range_type = sanitize_module_name(iri_str.split("/")[-1].split("#")[-1])
                        dependencies.append(f"{range_type}Module")
                        range_info = f"iri: {iri_str}"
                    elif isinstance(range_cls, URIRef):
                        iri_str = str(range_cls)
                        range_type = sanitize_module_name(iri_str.split("/")[-1].split("#")[-1])
                        dependencies.append(f"{range_type}Module")
                        range_info = f"URIRef: {iri_str}"

                properties.append({
                    "name": prop_name,
                    "range": range_type,
                    "iri": str(getattr(prop, "iri", "")),
                })
                seen_property_names.add(prop_name)
                log_debug(f"✔ Restriction: {prop_name} → {range_type} ({range_info})")

            except Exception as e:
                log_debug(f"[ERROR] Failed to process restriction on '{cls.name}': {e}")

    # --- Handle EMMO-style direct properties ---
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
                val = class_prop[0]
                if hasattr(val, "prefLabel") and val.prefLabel:
                    sanitized_range = sanitize_module_name(extract_label(val.prefLabel[0]))
                    dependencies.append(f"{sanitized_range}Module")
                elif hasattr(val, "name"):
                    sanitized_range = sanitize_module_name(val.name)
                    dependencies.append(f"{sanitized_range}Module")
                elif hasattr(val, "iri"):
                    iri_str = str(val.iri)
                    sanitized_range = sanitize_module_name(iri_str.split("/")[-1])

            properties.append({
                "name": sanitized_name,
                "range": sanitized_range,
                "iri": str(getattr(prop, "iri", "")),
            })
            seen_property_names.add(sanitized_name)
            log_debug(f"✔ Direct property: {sanitized_name} → {sanitized_range}")

        except Exception as e:
            log_debug(f"[ERROR] Failed to process direct property on '{cls.name}': {e}")

    # --- Handle schema.org-style properties using rdfs:domain ---
    try:
        for prop in cls.namespace.ontology.properties():
            if not hasattr(prop, "domain"):
                continue

            if cls not in prop.domain:
                continue

            prop_name = sanitize_module_name(getattr(prop, "name", "unknown_property"))
            if prop_name in seen_property_names:
                continue

            range_cls = list(prop.range)[0] if prop.range else None
            range_type = "str"
            range_info = "fallback"

            if range_cls:
                if hasattr(range_cls, "prefLabel") and range_cls.prefLabel:
                    range_type = sanitize_module_name(extract_label(range_cls.prefLabel[0]))
                    dependencies.append(f"{range_type}Module")
                    range_info = f"prefLabel: {range_cls.prefLabel[0]}"
                elif hasattr(range_cls, "name"):
                    range_type = sanitize_module_name(range_cls.name)
                    dependencies.append(f"{range_type}Module")
                    range_info = f"name: {range_cls.name}"
                elif hasattr(range_cls, "iri"):
                    iri_str = str(range_cls.iri)
                    range_type = sanitize_module_name(iri_str.split("/")[-1].split("#")[-1])
                    dependencies.append(f"{range_type}Module")
                    range_info = f"iri: {iri_str}"
                elif isinstance(range_cls, URIRef):
                    iri_str = str(range_cls)
                    range_type = sanitize_module_name(iri_str.split("/")[-1].split("#")[-1])
                    dependencies.append(f"{range_type}Module")
                    range_info = f"URIRef: {iri_str}"

            properties.append({
                "name": prop_name,
                "range": range_type,
                "iri": str(getattr(prop, "iri", "")),
            })
            seen_property_names.add(prop_name)
            log_debug(f"✔ RDF-style property: {prop_name} → {range_type} ({range_info})")

    except Exception as e:
        log_debug(f"[ERROR] Failed schema.org-style fallback on '{cls.name}': {e}")

    return properties, list(set(dependencies))



def get_parent_classes(cls):
    parent_classes = []
    if cls.is_a:
        for parent in cls.is_a:
            if parent.__class__.__name__ == "Restriction":
                continue
            if hasattr(parent, "prefLabel") and parent.prefLabel:
                parent_classes.append(extract_label(parent.prefLabel[0]))
            elif hasattr(parent, "label") and parent.label:
                parent_classes.append(extract_label(parent.label[0]))
            elif hasattr(parent, "iri"):
                iri_str = str(parent.iri)
                iri_suffix = iri_str.split("/")[-1].split("#")[-1]
                parent_classes.append(sanitize_module_name(iri_suffix))
    return parent_classes if parent_classes else ["LinkedDataModel"]
