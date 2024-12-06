"""
Ontology Module
---------------

This module handles ontology loading and extraction, including class and property handling.
"""

from .loader import load_ontology
from .extractor import extract_classes, extract_properties, get_parent_classes

__all__ = [
    "load_ontology",
    "extract_classes",
    "extract_properties",
    "get_parent_classes",
]
