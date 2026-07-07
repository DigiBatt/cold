import json

from cold.models import core as core_models


def make_mass_fraction(value: float) -> core_models.MaterialProperty:
    return core_models.MaterialProperty.from_quantity(
        value,
        "UnitOne",
        quantity_label="MassFraction",
        quantity_iri="https://w3id.org/emmo/domain/battery#MassFraction",
    )


# Define basic substances
lithium = core_models.ChemicalSubstance(label="Lithium Foil")
mnO2 = core_models.ChemicalSubstance(label="Manganese Dioxide Powder")
ec = core_models.ChemicalSubstance(label="Ethylene Carbonate")
emc = core_models.ChemicalSubstance(label="Ethyl Methyl Carbonate")
lipf6 = core_models.ChemicalSubstance(label="LiPF6 salt")

# Annotate solvent composition
ec.add_property(make_mass_fraction(0.3))
emc.add_property(make_mass_fraction(0.7))
lipf6.add_property(make_mass_fraction(0.127))

electrolyte = core_models.Electrolyte(
    label="LP57",
    hasSolvent=ec,
    hasSolute=lipf6,
)

# Build electrodes using helper factory
positive_electrode = core_models.factory.build_electrode(
    active_material=mnO2,
    label="Positive electrode",
)
negative_electrode = core_models.factory.build_electrode(
    active_material=lithium,
    label="Negative electrode",
)

# Assemble final cell using curated preset
cell = core_models.factory.build_cr2032_cell(
    positive_electrode=positive_electrode,
    negative_electrode=negative_electrode,
    electrolyte=electrolyte,
)

# Serialize to JSON-LD
json_ld = cell.to_jsonld()
print(json.dumps(json_ld, indent=4))

