"""
Models Module
-------------

This module handles the generation and customization of Pydantic models based on ontology data.
"""

from .generator import generate_pydantic_classes
from .customizations import customizations

__all__ = [
    "generate_pydantic_classes",
    "customizations",
]
