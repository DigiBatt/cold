from __future__ import annotations

from typing import List, Optional

from pydantic import Field

from .base import LinkedDataValue, OntologyBackedModel
from .components import (
    CellCase,
    CellHardware,
    Component,
    Electrolyte,
    Electrode,
)


class BatteryCell(OntologyBackedModel):
    """High-level representation of a battery cell."""

    ontology_iri = "https://w3id.org/emmo/domain/battery#ElectrochemicalCell"
    ontology_label = "ElectrochemicalCell"

    label: Optional[str] = Field(None, alias="rdfs:label")
    hasPositiveElectrode: Optional[Electrode] = Field(None, alias="hasPositiveElectrode")
    hasNegativeElectrode: Optional[Electrode] = Field(None, alias="hasNegativeElectrode")
    hasElectrolyte: Optional[Electrolyte] = Field(None, alias="hasElectrolyte")
    hasCase: Optional[CellCase] = Field(None, alias="hasCase")
    hasHardware: List[CellHardware] = Field(default_factory=list, alias="hasHardware")
    hasProperty: List[LinkedDataValue] = Field(default_factory=list, alias="hasProperty")

    def add_property(self, prop: LinkedDataValue) -> None:
        self.hasProperty.append(prop)

    def add_hardware(self, hardware: CellHardware) -> None:
        self.hasHardware.append(hardware)


class CoinCell(BatteryCell):
    ontology_iri = "https://w3id.org/emmo/domain/battery#CoinCell"
    ontology_label = "CoinCell"

    def configure_case(self, diameter_mm: float, thickness_mm: float) -> None:
        case = self.hasCase or CellCase(label="Coin cell case")
        case.hasProperty.extend(
            [
                LinkedDataValue.from_quantity(
                    diameter_mm,
                    "MilliMetre",
                    quantity_label="Diameter",
                    quantity_iri="https://w3id.org/emmo/domain/battery#Diameter",
                ),
                LinkedDataValue.from_quantity(
                    thickness_mm,
                    "MilliMetre",
                    quantity_label="Thickness",
                    quantity_iri="https://w3id.org/emmo/domain/battery#Thickness",
                ),
            ]
        )
        self.hasCase = case


class CR2032Cell(CoinCell):
    """Preset for a CR2032-format cell."""

    ontology_iri = "https://w3id.org/emmo/domain/battery#CR2032"
    ontology_label = "CR2032"

    def __init__(self, **data):
        super().__init__(**data)
        if not self.hasCase:
            self.configure_case(20.0, 3.2)


class CylindricalCell(BatteryCell):
    ontology_iri = "https://w3id.org/emmo/domain/battery#CylindricalCell"
    ontology_label = "CylindricalCell"

    hasCan: Optional[Component] = Field(None, alias="hasCan")

    def configure_dimensions(self, diameter_mm: float, length_mm: float) -> None:
        self.add_property(
            LinkedDataValue.from_quantity(
                diameter_mm,
                "MilliMetre",
                quantity_label="Diameter",
                quantity_iri="https://w3id.org/emmo/domain/battery#Diameter",
            )
        )
        self.add_property(
            LinkedDataValue.from_quantity(
                length_mm,
                "MilliMetre",
                quantity_label="Length",
                quantity_iri="https://w3id.org/emmo/domain/battery#Length",
            )
        )


class INR18650Cell(CylindricalCell):
    ontology_iri = "https://w3id.org/emmo/domain/battery#INR18650"
    ontology_label = "INR18650"

    def __init__(self, **data):
        super().__init__(**data)
        self.configure_dimensions(18.0, 65.0)
