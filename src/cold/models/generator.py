import os
from jinja2 import Template
from .customizations import customizations
from ..ontology.extractor import extract_properties, get_parent_classes
from ..utils.sanitizers import sanitize_module_name
from ..utils.helpers import extract_label

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
            "imports": []  # Custom classes may not need additional imports
        }

        # Render and write the template
        class_code = render_class(context, template)
        write_class_file(output_dir, class_name, class_code)
        generated_classes.append((class_name, sanitize_module_name(class_name)))

        print(f"Generated top-level Pydantic class: {class_name} (sanitized as {sanitize_module_name(class_name)}Module)")

    # Generate ontology-based classes
    for idx, cls in enumerate(classes):
        if max_classes and idx >= max_classes:
            print(f"Reached the maximum class generation limit of {max_classes}.")
            break

        try:
            # Extract class metadata
            raw_pref_label = cls.prefLabel[0] if hasattr(cls, "prefLabel") and cls.prefLabel else None
            class_name = extract_label(raw_pref_label) if raw_pref_label else "UnnamedClass"

        

            #class_name = cls.prefLabel[0]
            sanitized_name = sanitize_module_name(class_name)
            properties, dependencies = extract_properties(cls)

            # Create context for rendering the class
            context = {
                "class_name": class_name,
                "properties": properties,
                "parent_classes": get_parent_classes(cls),
                "methods": [],
                "custom_models": custom_models,
                "imports": dependencies,  # Add dependencies for imports
            }

            # Apply customizations
            context = apply_customizations(class_name, context)

            #print(context)

            # Render and write the template
            class_code = render_class(context, template)
            write_class_file(output_dir, class_name, class_code)
            generated_classes.append((class_name, sanitized_name))

            #print(f"Generated Pydantic class: {class_name} (sanitized as {sanitized_name}Module)")
        except Exception as e:
            #print(f"Error generating class for '{getattr(cls, 'prefLabel', ['Unknown'])[0]}': {e}")
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
    Apply customizations to a class based on its name.

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

        # Add parent classes if specified
        if "parent_classes" in custom:
            context["parent_classes"].extend(custom["parent_classes"])

        # Add properties if specified
        if "properties" in custom:
            for prop in custom["properties"]:
                context["properties"].append({
                    "name": prop["name"],
                    "range": prop.get("range", "str"),
                    "alias": prop.get("alias", prop["name"]),
                    "default": prop.get("default", None),  # Default is None if not specified
                    "exclude": prop.get("exclude", False),  # Handle exclude for serialization
                })

        # Add custom imports if specified
        if "imports" in custom:
            context.setdefault("additional_imports", []).extend(custom["imports"])

        # Add custom methods if specified
        if "methods" in custom:
            context["methods"].extend(custom["methods"])

    return context


def generate_lazy_init(output_dir, generated_classes):
    """
    Generate an __init__.py file for lazy loading of generated classes.

    Args:
        output_dir (str): Directory where the __init__.py file will be created.
        generated_classes (list): List of tuples (original_class_name, sanitized_name).
    """
    init_file_path = os.path.join(output_dir, "__init__.py")
    with open(init_file_path, "w", encoding="utf-8") as f:
        # Write all classes to __all__
        f.write("__all__ = [\n")
        for class_name, sanitized_name in generated_classes:
            f.write(f"    '{sanitized_name}',\n")
        f.write("]\n\n")

        # Add lazy loading logic
        f.write("""
import importlib

def __getattr__(name):
    if name in __all__:
        module = importlib.import_module(f".{name}Module", package=__name__)
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")
""")
