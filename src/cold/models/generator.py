import os
from jinja2 import Template
from .customizations import customizations
from ..ontology.extractor import extract_properties, get_parent_classes
from ..utils.sanitizers import sanitize_module_name
from ..utils.helpers import extract_label, get_prefLabel


def generate_pydantic_classes(classes, template_path, output_dir, max_classes=None):
    """
    Generate Pydantic classes from ontology classes.

    Args:
        classes (list): List of ontology classes to generate models for.
        template_path (str): Path to the Jinja2 template file.
        output_dir (str): Directory to write the generated Pydantic model files.
        max_classes (int, optional): Limit the number of classes to generate. Defaults to None.
    """
    # Load the template
    with open(template_path, "r", encoding="utf-8") as template_file:
        template = Template(template_file.read())

    custom_models = ["LinkedDataModel", "NumericalPart"]  # Define your custom models here
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    generated_classes = []  # Keep track of all generated class names and sanitized names

    # Generate explicitly defined top-level classes in customizations
    for class_name, customization in customizations.items():
        context = {
            "class_name": class_name,
            "properties": customization.get("properties", []),
            "parent_classes": customization.get("parent_classes", ["BaseModel"]),
            "methods": customization.get("methods", []),
            "custom_models": custom_models,
            "additional_imports": customization.get("imports", []),  # Use the imports from the customization
        }

        # Render and write the template
        class_code = render_class(context, template)
        write_class_file(output_dir, class_name, class_code)
        generated_classes.append((class_name, sanitize_module_name(class_name)))

        print(
            f"Generated top-level Pydantic class: {class_name} (sanitized as {sanitize_module_name(class_name)}Module)"
        )

    # Generate ontology-based classes
    for idx, cls in enumerate(classes):
        if max_classes and idx >= max_classes:
            print(f"Reached the maximum class generation limit of {max_classes}.")
            break

        try:
            raw_pref_label = cls.prefLabel[0] if hasattr(cls, "prefLabel") and cls.prefLabel else None
            class_name = extract_label(raw_pref_label) if raw_pref_label else "UnnamedClass"
            sanitized_name = sanitize_module_name(class_name)

            # Extract properties with knowledge of parent classes
            properties, dependencies = extract_properties(cls)

            if class_name == "EMMO":
                # Clear dependencies completely
                # Normalize the dependencies to their base names
                normalized_dependencies = {dep.replace("Module", "") for dep in dependencies}
                dependencies = []

                # Filter properties where the range matches any normalized dependency
                properties = [
                    prop for prop in properties if prop["range"] not in normalized_dependencies
                ]



            # Create context for rendering the class
            context = {
                "class_name": class_name,
                "properties": properties,
                "parent_classes": get_parent_classes(cls),
                "methods": [],
                "custom_models": custom_models,
                "imports": dependencies,
            }

            # Apply customizations
            context = apply_customizations(class_name, context)

            # Render and write the template
            class_code = render_class(context, template)
            write_class_file(output_dir, class_name, class_code)
            generated_classes.append((class_name, sanitized_name))
        except Exception as e:
            print(f"Error generating class for '{class_name}': {e}")
            continue


    # Generate __init__.py for lazy loading
    generate_lazy_init(output_dir, generated_classes)

    print(f"Total Pydantic models generated: {len(generated_classes)}")


def render_class(context, template):
    """
    Render a class using the provided context and template.

    Args:
        context (dict): Context dictionary for rendering the template.
        template (Template): Jinja2 template.

    Returns:
        str: Rendered class code.
    """
    return template.render(context)


def write_class_file(output_dir, class_name, class_code):
    """
    Write the generated class code to a file.

    Args:
        output_dir (str): Directory to write the file.
        class_name (str): Name of the class.
        class_code (str): Generated class code.
    """
    sanitized_name = sanitize_module_name(class_name)
    file_path = os.path.join(output_dir, f"{sanitized_name}Module.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(class_code)


def apply_customizations(class_name, context):
    """
    Apply customizations to a class based on its name, merging them with the autogenerated data.

    Args:
        class_name (str): The name of the class being generated.
        context (dict): The current context dictionary for the class, which includes
                        properties, parent_classes, methods, imports, and other metadata.

    Returns:
        dict: The updated context with the applied customizations.
    """
    # Check if the class has any customizations defined
    if class_name in customizations:
        custom = customizations[class_name]

        # Merge parent classes
        if class_name == "EMMO":
            # Ensure EMMO has only LinkedDataModel as its parent class
            context["parent_classes"] = ["LinkedDataModel"]
        else:
            # Add any custom parent classes without overwriting existing ones
            for parent in custom.get("parent_classes", []):
                if parent not in context["parent_classes"]:
                    context["parent_classes"].append(parent)

        # Merge properties: Add custom properties without overwriting autogenerated ones
        custom_properties = {prop["name"]: prop for prop in custom.get("properties", [])}
        auto_properties = {prop["name"]: prop for prop in context.get("properties", [])}
        merged_properties = {**auto_properties, **custom_properties}  # Custom properties take precedence
        context["properties"] = list(merged_properties.values())

        # Handle instantiated_defaults
        instantiated_defaults = custom.get("instantiated_defaults", [])
        for prop in context["properties"]:
            if prop["name"] in instantiated_defaults:
                prop["default"] = f"{prop['range']}()"

        # Merge imports: Add custom imports without duplicating
        context.setdefault("additional_imports", []).extend(custom.get("imports", []))
        context["additional_imports"] = list(set(context["additional_imports"]))  # Deduplicate imports

        # Merge methods: Add custom methods in addition to autogenerated methods
        context["methods"].extend(custom.get("methods", []))

    return context







def generate_lazy_init(output_dir, generated_classes):
    """
    Generate or update an __init__.py file for lazy loading of generated classes.

    Args:
        output_dir (str): Directory where the __init__.py file will be created or updated.
        generated_classes (list): List of tuples (original_class_name, sanitized_name).
    """
    init_file_path = os.path.join(output_dir, "__init__.py")

    # Initialize a set to track existing entries in __all__
    existing_classes = set()
    lazy_loading_code = """
import importlib

def __getattr__(name):
    if name in __all__:
        module = importlib.import_module(f".{name}Module", package=__name__)
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
"""

    # Read existing __init__.py file to collect current __all__ entries
    if os.path.exists(init_file_path):
        with open(init_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            in_all_block = False
            for line in lines:
                stripped_line = line.strip()
                if stripped_line == "__all__ = [":
                    in_all_block = True
                    continue
                if in_all_block:
                    if stripped_line == "]":
                        in_all_block = False
                    else:
                        # Extract the class name from lines like 'ClassName',
                        if stripped_line.endswith(","):  # Handle trailing commas
                            stripped_line = stripped_line[:-1]
                        class_name = stripped_line.strip("'")
                        existing_classes.add(class_name)

    # Add new classes to the set of existing classes
    for _, sanitized_name in generated_classes:
        existing_classes.add(sanitized_name)

    # Write the updated __init__.py file
    with open(init_file_path, "w", encoding="utf-8") as f:
        # Write the complete __all__ list
        f.write("__all__ = [\n")
        for sanitized_name in sorted(existing_classes):  # Sort for consistency
            f.write(f"    '{sanitized_name}',\n")
        f.write("]\n\n")

        # Write the lazy loading logic
        f.write(lazy_loading_code)
