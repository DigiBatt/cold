import re
import keyword

_PYTHON_KEYWORDS = set(keyword.kwlist)

def sanitize_module_name(name: str) -> str:
    """
    Sanitize a string to make it a valid Python module name.

    - Replaces spaces and dashes with underscores.
    - Prefixes with 'N_' if it starts with a digit.
    - Replaces other invalid characters with underscores.
    - Ensures the name does not conflict with Python keywords.

    Args:
        name (str): The original name to sanitize.

    Returns:
        str: The sanitized module name.
    """
    # Basic normalization
    sanitized = name.replace("-", "_").replace(" ", "_").strip()

    # Replace non-alphanumeric characters with underscores
    sanitized = re.sub(r'\W', '_', sanitized)

    # Prefix with 'N_' if it starts with a digit
    if sanitized and sanitized[0].isdigit():
        sanitized = f"N_{sanitized}"

    # Avoid Python keywords
    if sanitized in _PYTHON_KEYWORDS:
        sanitized = f"{sanitized}_keyword"

    return sanitized



def is_valid_identifier(name: str) -> bool:
    """
    Check if a string is a valid Python identifier.

    Args:
        name (str): The name to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return name.isidentifier() and name not in _PYTHON_KEYWORDS


def sanitize_class_name(name: str) -> str:
    """
    Sanitize a string to make it a valid Python class name.

    - Capitalizes each word.
    - Removes invalid characters.
    - Ensures compatibility with Python naming conventions.

    Args:
        name (str): The original name to sanitize.

    Returns:
        str: The sanitized class name.
    """
    # Replace invalid characters with spaces, capitalize each word, and join without spaces
    sanitized = ''.join(word.capitalize() for word in re.split(r'\W+', name.strip()) if word)

    # Ensure the name doesn't conflict with Python keywords
    if sanitized in _PYTHON_KEYWORDS:
        sanitized = f"{sanitized}Class"

    return sanitized


def sanitize_property_name(name: str) -> str:
    """
    Sanitize a string to make it a valid Python property name.

    - Converts spaces and invalid characters to underscores.
    - Strips leading and trailing whitespace.
    - Ensures the name doesn't conflict with Python keywords.

    Args:
        name (str): The original property name.

    Returns:
        str: The sanitized property name.
    """
    sanitized = re.sub(r'\W|^(?=\d)', '_', name.strip())

    # Ensure the name doesn't conflict with Python keywords
    if sanitized in _PYTHON_KEYWORDS:
        sanitized = f"{sanitized}_property"

    return sanitized


def clean_iri(iri: str) -> str:
    """
    Extract a clean, human-readable identifier from an IRI.

    Args:
        iri (str): The original IRI.

    Returns:
        str: A clean identifier derived from the IRI.
    """
    # Extract the fragment after the last '/' or '#'
    match = re.search(r'[\/#]([^\/#]*)$', iri)
    return match.group(1) if match else iri


# List of Python keywords for validation
_PYTHON_KEYWORDS = {
    "False", "None", "True", "and", "as", "assert", "async", "await", "break",
    "class", "continue", "def", "del", "elif", "else", "except", "finally",
    "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
}
