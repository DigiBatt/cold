from __future__ import annotations

from typing import List, Optional

from pydantic import Field

from .base import LinkedDataValue, OntologyBackedModel
from .materials import ChemicalSubstance, MaterialProperty


class Component(OntologyBackedModel):
    """Physical component used within a device."""

    ontology_iri = "https://w3id.org/emmo/domain/battery#Component"
    ontology_label = "Component"

    label: Optional[str] = Field(None, alias="rdfs:label")
    hasMaterial: Optional[ChemicalSubstance] = Field(None, alias="hasMaterial")
    hasProperty: List[MaterialProperty] = Field(default_factory=list)

    def add_property(self, prop: MaterialProperty) -> None:
        self.hasProperty.append(prop)


class Electrode(Component):
    ontology_iri = "https://w3id.org/emmo/domain/battery#Electrode"
    ontology_label = "Electrode"

    hasActiveMaterial: Optional[ChemicalSubstance] = Field(None, alias="hasActiveMaterial")
    hasCurrentCollector: Optional["CurrentCollector"] = Field(None, alias="hasCurrentCollector")
    hasBinder: Optional["Binder"] = Field(None, alias="hasBinder")
    hasConductiveAdditive: Optional["ConductiveAdditive"] = Field(None, alias="hasConductiveAdditive")


class Electrolyte(Component):
    ontology_iri = "https://w3id.org/emmo/domain/battery#Electrolyte"
    ontology_label = "Electrolyte"

    hasSolvent: Optional[ChemicalSubstance] = Field(None, alias="hasSolvent")
    hasSolute: Optional[ChemicalSubstance] = Field(None, alias="hasSolute")


class CurrentCollector(Component):
    ontology_iri = "https://w3id.org/emmo/domain/battery#CurrentCollector"
    ontology_label = "CurrentCollector"


class Binder(Component):
    ontology_iri = "https://w3id.org/emmo/domain/battery#Binder"
    ontology_label = "Binder"


class ConductiveAdditive(Component):
    ontology_iri = "https://w3id.org/emmo/domain/battery#ConductiveAdditive"
    ontology_label = "ConductiveAdditive"


class CellCase(Component):
    ontology_iri = "https://w3id.org/emmo/domain/battery#CellCase"
    ontology_label = "CellCase"

    hasProperty: List[LinkedDataValue] = Field(default_factory=list)


class CellHardware(Component):
    ontology_iri = "https://w3id.org/emmo/domain/battery#CellHardware"
    ontology_label = "CellHardware"

