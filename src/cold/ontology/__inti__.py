"""
Ontology Module
---------------

This module handles ontology loading and extraction, including class and property handling.
"""

from .loader import load_ontology_emmo, load_ontology_other
from .extractor import extract_classes, extract_classes_emmo, extract_properties, get_parent_classes
from .formatter import format_ontology
from .importer import import_ontology

__all__ = [
    "format_ontology",
    "import_ontology",
    "load_ontology_emmo",
    "load_ontology_other",
    "extract_classes",
    "extract_classes_emmo",
    "extract_properties",
    "get_parent_classes",
]
