from __future__ import annotations

from typing import Iterable, Optional

from .components import Binder, ConductiveAdditive, Electrode
from .devices import CR2032Cell, INR18650Cell
from .materials import ChemicalSubstance, MaterialProperty


def build_electrode(
    *,
    active_material: ChemicalSubstance,
    label: Optional[str] = None,
    binder: Optional[Binder] = None,
    conductive_additive: Optional[ConductiveAdditive] = None,
    extra_properties: Optional[Iterable[MaterialProperty]] = None,
) -> Electrode:
    electrode = Electrode(
        rdfs__label=label,
        hasActiveMaterial=active_material,
    )
    if binder:
        electrode.hasBinder = binder
    if conductive_additive:
        electrode.hasConductiveAdditive = conductive_additive
    if extra_properties:
        for prop in extra_properties:
            electrode.add_property(prop)
    return electrode


def build_cr2032_cell(
    *,
    positive_electrode: Electrode,
    negative_electrode: Electrode,
    electrolyte,
):
    return CR2032Cell(
        hasPositiveElectrode=positive_electrode,
        hasNegativeElectrode=negative_electrode,
        hasElectrolyte=electrolyte,
    )


def build_inr18650_cell(
    *,
    positive_electrode: Electrode,
    negative_electrode: Electrode,
    electrolyte,
):
    return INR18650Cell(
        hasPositiveElectrode=positive_electrode,
        hasNegativeElectrode=negative_electrode,
        hasElectrolyte=electrolyte,
    )
