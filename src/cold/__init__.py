"""
cold
----

A Python package for generating and validating linked data instances
based on ontologies using Pydantic models.

Modules:
    ontology: Handles ontology loading and extraction.
    models: Contains Pydantic model generation and customizations.
    utils: Utility functions for sanitization and validation.

Usage:
    - Load ontology: `from cold.ontology.loader import load_ontology`
    - Extract classes: `from cold.ontology.extractor import extract_classes`
    - Generate models: `from cold.models.generator import generate_pydantic_classes`
"""

# Ontology Handling
from .ontology.formatter import format_ontology
from .ontology.importer import import_ontology
from .ontology.loader import load_ontology
from .ontology.extractor import (
    extract_classes,
    extract_properties,
    get_parent_classes,
)

# Model Generation
from .models.generator import generate_pydantic_classes

# Utilities
from .utils.sanitizers import sanitize_module_name
from .utils.helpers import get_prefLabel, extract_label
from .utils.access import *

# Package Metadata
__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Public API
__all__ = [
    "format_ontology",
    "import_ontology",
    "load_ontology",
    "extract_classes",
    "extract_properties",
    "get_parent_classes",
    "generate_pydantic_classes",
    "sanitize_module_name",
]
