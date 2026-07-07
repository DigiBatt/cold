import json

from cold.models import core as core_models


# Define core materials
lithium = core_models.ChemicalSubstance(label="Lithium metal")
mnO2 = core_models.ChemicalSubstance(label="Manganese dioxide")
electrolyte_solvent = core_models.ChemicalSubstance(label="LP57 solvent")
lipf6 = core_models.ChemicalSubstance(label="LiPF6")

# Build electrodes
negative_electrode = core_models.Electrode(
    label="Negative electrode",
    hasActiveMaterial=lithium,
)
positive_electrode = core_models.Electrode(
    label="Positive electrode",
    hasActiveMaterial=mnO2,
)

# Build electrolyte
electrolyte = core_models.Electrolyte(
    label="LP57 electrolyte",
    hasSolvent=electrolyte_solvent,
    hasSolute=lipf6,
)

# Instantiate cell preset
cell = core_models.CR2032Cell(
    label="CR2032 coin cell",
    hasNegativeElectrode=negative_electrode,
    hasPositiveElectrode=positive_electrode,
    hasElectrolyte=electrolyte,
)

cell.add_property(
    core_models.LinkedDataValue.from_quantity(
        3.2,
        "Volt",
        quantity_label="NominalVoltage",
        quantity_iri="https://w3id.org/emmo/domain/battery#NominalVoltage",
    )
)

# Serialize to JSON-LD
json_ld = cell.to_jsonld()
print(json.dumps(json_ld, indent=4))
