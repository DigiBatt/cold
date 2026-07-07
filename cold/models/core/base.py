from __future__ import annotations

from typing import Any, ClassVar, Dict, List, Optional, Union

from pydantic import Field, root_validator

from cold.models.custom.LinkedDataModelModule import LinkedDataModel


class OntologyBackedModel(LinkedDataModel):
    """
    Thin wrapper around ``LinkedDataModel`` that remembers the ontology class metadata.

    Subclasses should set ``ontology_iri`` and ``ontology_label`` so default ``@type`` and IRI
    information are automatically injected into serialized JSON-LD.
    """

    ontology_iri: ClassVar[str] = ""
    ontology_label: ClassVar[str] = ""

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True
        validate_assignment = True

    @root_validator(pre=True)
    def _inject_class_metadata(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        values.setdefault("class_iri", cls.ontology_iri or None)
        values.setdefault("class_name", cls.ontology_label or cls.__name__)
        return values


class LinkedDataValue(OntologyBackedModel):
    """
    Represents a simple quantity/value pair with the associated ontology predicate.

    Example: ``MaterialProperty(value=0.5, unit="UnitOne", property_iri="...MassFraction")``.
    """

    value: Union[int, float, str, bool] = Field(..., alias="hasValue")
    unit: Optional[str] = Field(None, alias="hasUnit")
    unit_iri: Optional[str] = Field(None, alias="hasUnitIri")
    property_iri: Optional[str] = Field(None, alias="propertyIri")

    @classmethod
    def from_quantity(
        cls,
        value: Union[int, float],
        unit: str,
        *,
        quantity_label: str,
        quantity_iri: str,
        unit_iri: Optional[str] = None,
    ) -> "LinkedDataValue":
        """Convenience factory for physical quantities."""
        return cls(
            hasValue=value,
            hasUnit=unit,
            hasUnitIri=unit_iri,
            propertyIri=quantity_iri,
            class_name=quantity_label,
        )
