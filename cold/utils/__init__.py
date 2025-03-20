"""
Utils Module
------------

This module provides utility functions for sanitization, validation, and label extraction.
"""

from .sanitizers import sanitize_module_name, sanitize_class_name, sanitize_property_name, clean_iri
from .helpers import extract_label, get_prefLabel
from .access import *

__all__ = [
    "sanitize_module_name",
    "sanitize_class_name",
    "sanitize_property_name",
    "clean_iri",
    "extract_label",
]
