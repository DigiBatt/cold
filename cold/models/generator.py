import os
import json
from jinja2 import Template
from .customizations import customizations
from ..ontology.extractor import extract_properties, get_parent_classes
from ..utils.sanitizers import sanitize_module_name
from ..utils.helpers import extract_label


def generate_pydantic_classes(class_prefix_pairs, template_path, output_dir, max_classes=None):
    """
    Generate Pydantic classes from ontology classes.

    Args:
        class_prefix_pairs (list): List of tuples (ontology class, source prefix).
        template_path (str): Path to the Jinja2 template file.
        output_dir (str): Directory to write the generated Pydantic model files.
        max_classes (int, optional): Limit the number of classes to generate. Defaults to None.
    """
    with open(template_path, "r", encoding="utf-8") as template_file:
        template = Template(template_file.read())

    custom_models = ["LinkedDataModel", "NumericalPart"]
    os.makedirs(output_dir, exist_ok=True)
    generated_classes = []
    ignore_list = set(customizations.get("IGNORE", []))

    for idx, (cls, prefix) in enumerate(class_prefix_pairs):
        class_name = extract_label(cls)

        if class_name in ignore_list:
            print(f"Skipping ignored class: {class_name}")
            continue

        if max_classes and idx >= max_classes:
            print(f"Reached the maximum class generation limit of {max_classes}.")
            break

        try:
            properties, dependencies = extract_properties(cls)

            if class_name == "EMMO":
                dependencies = []
                normalized_dependencies = {dep.replace("Module", "") for dep in dependencies}
                properties = [
                    prop for prop in properties if prop["range"] not in normalized_dependencies
                ]

            custom = customizations.get(class_name, {})
            excluded_props = set(custom.get("exclude_properties", []))
            properties = [prop for prop in properties if prop["name"] not in excluded_props]

            context = {
                "class_name": class_name,
                "properties": properties,
                "parent_classes": get_parent_classes(cls),
                "methods": [],
                "custom_models": custom_models,
                "imports": dependencies,
                "additional_imports": custom.get("imports", []),
                "prefix": prefix,
            }

            context = apply_customizations(class_name, context)

            class_code = render_class(context, template)
            sanitized_class_name = sanitize_module_name(class_name)
            module_filename = f"{sanitized_class_name}__{prefix}"
            write_class_file(output_dir, class_name, class_code, prefix)
            generated_classes.append((class_name, module_filename))
        except Exception as e:
            print(f"Error generating class for '{class_name}': {e}")
            continue

    generate_lazy_init(output_dir, generated_classes)
    print(f"Total Pydantic models generated: {len(generated_classes)}")


def render_class(context, template):
    return template.render(context)


def write_class_file(output_dir, class_name, class_code, prefix):
    sanitized_class_name = sanitize_module_name(class_name)
    filename = f"{sanitized_class_name}__{prefix}.py"
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(class_code)


def apply_customizations(class_name, context):
    if class_name not in customizations:
        return context

    custom = customizations[class_name]

    if class_name == "EMMO":
        context["parent_classes"] = ["LinkedDataModel"]
    else:
        for parent in custom.get("parent_classes", []):
            if parent not in context["parent_classes"]:
                context["parent_classes"].append(parent)

    excluded_parents = set(custom.get("exclude_parent_classes", []))
    context["parent_classes"] = [
        p for p in context["parent_classes"] if p not in excluded_parents
    ]

    custom_props = {p["name"]: p for p in custom.get("properties", [])}
    auto_props = {p["name"]: p for p in context.get("properties", [])}
    merged_props = {**auto_props, **custom_props}
    context["properties"] = list(merged_props.values())

    for prop in context["properties"]:
        if prop["name"] in custom.get("instantiated_defaults", []):
            prop["default"] = f"{prop['range']}()"

    context.setdefault("additional_imports", []).extend(custom.get("imports", []))
    context["additional_imports"] = list(set(context["additional_imports"]))

    context["methods"].extend(custom.get("methods", []))
    return context


def generate_lazy_init(output_dir, generated_classes):
    init_file_path = os.path.join(output_dir, "__init__.py")
    class_to_module = {cls: mod for cls, mod in generated_classes}
    existing_classes = set(class_to_module.keys())

    lazy_loading_code = f"""
import importlib

_module_map = {json.dumps(class_to_module, indent=4)}

def __getattr__(name):
    if name in __all__:
        module_name = _module_map[name]
        module = importlib.import_module(f".{{module_name}}", package=__name__)
        return getattr(module, name)
    raise AttributeError(f"module {{__name__}} has no attribute {{name}}")
"""

    with open(init_file_path, "w", encoding="utf-8") as f:
        f.write("__all__ = [\n")
        for name in sorted(existing_classes):
            f.write(f"    '{name}',\n")
        f.write("]\n\n")
        f.write(lazy_loading_code)
