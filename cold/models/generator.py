import os
import json
from jinja2 import Template
from .customizations import customizations
from ..ontology.extractor import extract_properties, get_parent_classes
from ..utils.sanitizers import sanitize_module_name
from ..utils.helpers import extract_label


def generate_pydantic_classes(class_prefix_pairs, template_path, output_dir, max_classes=None):
    with open(template_path, "r", encoding="utf-8") as template_file:
        template = Template(template_file.read())

    custom_models = ["LinkedDataModel", "NumericalPart"]
    generated_classes = []
    ignore_list = set(customizations.get("IGNORE", []))

    for idx, (cls, prefix) in enumerate(class_prefix_pairs):
        class_name = extract_label(cls)

        if class_name in ignore_list or class_name[0].isdigit():
            print(f"Skipping class: {class_name}")
            continue

        if max_classes and idx >= max_classes:
            print(f"Reached max_classes limit of {max_classes}")
            break

        try:
            properties, dependencies = extract_properties(cls)

            # Always add class_name explicitly as a field
            properties.append({
                "name": "class_name",
                "range": "str",
                "iri": None,
                "default": f'"{class_name}"',
            })


            if class_name in {"EMMO", "Thing"}:
                dependencies = []
                normalized_deps = {dep.replace("Module", "") for dep in dependencies}
                properties = [prop for prop in properties if prop["range"] not in normalized_deps]

            custom = customizations.get(class_name, {})
            excluded_props = set(custom.get("exclude_properties", []))
            properties = [p for p in properties if p["name"] not in excluded_props]

            has_self_reference = any(p["range"] == class_name for p in properties)
            has_circular_import = any(p["range"] in [c for c, *_ in class_prefix_pairs] for p in properties)


            context = {
                "class_name": class_name,
                "properties": properties,
                "parent_classes": get_parent_classes(cls),
                "methods": [],
                "custom_models": custom_models,
                "imports": dependencies,
                "additional_imports": custom.get("imports", []),
                "has_self_reference": has_self_reference,
                "has_circular_import": has_circular_import,
            }

            context = apply_customizations(class_name, context)

            module_path = os.path.join(output_dir, prefix)
            os.makedirs(module_path, exist_ok=True)

            class_code = render_class(context, template)
            module_name = sanitize_module_name(class_name)
            write_class_file(module_path, module_name, class_code)

            generated_classes.append((class_name, module_name, prefix, f"{prefix}"))

        except Exception as e:
            print(f"Error generating class for '{class_name}': {e}")

    return generated_classes


def render_class(context, template):
    return template.render(context)


def write_class_file(module_path, module_name, class_code):
    file_path = os.path.join(module_path, f"{module_name}Module.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(class_code)


def apply_customizations(class_name, context):
    if class_name not in customizations:
        return context
    custom = customizations[class_name]

    if class_name in {"EMMO", "Thing"}:
        context["parent_classes"] = ["LinkedDataModel"]
    else:
        for parent in custom.get("parent_classes", []):
            if parent not in context["parent_classes"]:
                context["parent_classes"].append(parent)

    excluded_parents = set(custom.get("exclude_parent_classes", []))
    context["parent_classes"] = [p for p in context["parent_classes"] if p not in excluded_parents]

    merged_props = {p["name"]: p for p in context.get("properties", [])}
    merged_props.update({p["name"]: p for p in custom.get("properties", [])})
    context["properties"] = list(merged_props.values())

    # Remove object properties excluded by customization
    excluded_object_properties = set(custom.get("exclude_object_properties", []))
    context["properties"] = [
        prop for prop in context["properties"]
        if prop["name"] not in excluded_object_properties
    ]

    for prop in context["properties"]:
        if prop["name"] in custom.get("instantiated_defaults", []):
            prop["default"] = f"{prop['range']}()"

    context.setdefault("additional_imports", []).extend(custom.get("imports", []))
    context["additional_imports"] = list(set(context["additional_imports"]))
    context["methods"].extend(custom.get("methods", []))

    return context


def generate_lazy_init(output_dir, generated_classes):
    init_path = os.path.join(output_dir, "__init__.py")
    class_to_module = {cls: f"{module_path}.{mod}" for cls, mod, _, module_path in generated_classes}

    with open(init_path, "w", encoding="utf-8") as f:
        f.write("__all__ = [\n")
        for name in sorted(class_to_module.keys()):
            f.write(f"    '{name}',\n")
        f.write("]\n\n")

        for cls, mod_path in class_to_module.items():
            f.write(f"from .{mod_path}Module import {cls}\n")

        f.write(f"""

import importlib

_module_map = {json.dumps(class_to_module, indent=4)}

def __getattr__(name):
    if name in __all__:
        module_name = _module_map[name]
        module = importlib.import_module(f".{{module_name}}", package=__name__)
        return getattr(module, name)
    raise AttributeError(f"module {{__name__}} has no attribute {{name}}")
""")


def generate_top_level_init(output_dir, generated_classes):
    """
    Generates cold/__init__.py with lazy top-level imports
    """
    init_path = os.path.join("cold", "__init__.py")

    class_to_module = {
        cls: f"models.autogenerated.{prefix}.{mod}Module"
        for cls, mod, prefix, _ in generated_classes
    }

    # Determine which prefixes to expose as submodules
    prefixes = sorted({prefix for _, _, prefix, _ in generated_classes})

    with open(init_path, "w", encoding="utf-8") as f:
        f.write("__all__ = [\n")
        for cls in sorted(class_to_module.keys()):
            f.write(f"    '{cls}',\n")
        for prefix in prefixes:
            f.write(f"    '{prefix}',\n")
        f.write("]\n\n")

        # Explicit namespaces always available
        for prefix in prefixes:
            f.write(f"from .models.autogenerated import {prefix}\n")

        f.write("\nimport importlib\n\n")

        f.write("_class_to_module = {\n")
        for cls, mod_path in class_to_module.items():
            f.write(f"    '{cls}': '{mod_path}',\n")
        f.write("}\n\n")

        f.write("""\
def __getattr__(name):
    if name in _class_to_module:
        modpath = _class_to_module[name]
        mod = importlib.import_module(f".{modpath}", __name__)
        return getattr(mod, name)
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
""")



