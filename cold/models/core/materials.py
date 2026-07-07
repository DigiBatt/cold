from __future__ import annotations

from typing import List, Optional

from pydantic import Field

from .base import LinkedDataValue, OntologyBackedModel


class MaterialProperty(LinkedDataValue):
    """Physical characteristic tied to an ontology predicate."""

    ontology_iri = "https://w3id.org/emmo/domain/battery#Property"
    ontology_label = "Property"


class MaterialComposition(OntologyBackedModel):
    """Relationship linking a material to its constituents."""

    ontology_iri = "https://w3id.org/emmo/domain/battery#hasConstituent"
    ontology_label = "ConstituentRelation"

    constituent: "ChemicalSubstance" = Field(..., alias="hasConstituent")
    role: Optional[str] = Field(None, alias="hasRole")


class ChemicalSubstance(OntologyBackedModel):
    """Generic chemical substance."""

    ontology_iri = "https://w3id.org/emmo#ChemicalSubstance"
    ontology_label = "ChemicalSubstance"

    label: Optional[str] = Field(None, alias="rdfs:label")
    formula: Optional[str] = Field(None, alias="hasChemicalFormula")
    hasProperty: List[MaterialProperty] = Field(default_factory=list)
    hasConstituent: List[MaterialComposition] = Field(default_factory=list)

    def add_property(self, prop: MaterialProperty) -> None:
        self.hasProperty.append(prop)

    def add_constituent(self, constituent: "ChemicalSubstance", *, role: Optional[str] = None) -> None:
        self.hasConstituent.append(MaterialComposition(hasConstituent=constituent, hasRole=role))

