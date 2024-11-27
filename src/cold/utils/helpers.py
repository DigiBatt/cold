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
