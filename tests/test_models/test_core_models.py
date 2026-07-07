import json

from cold.models import core as core_models


def test_cr2032_curated_workflow():
    lithium = core_models.ChemicalSubstance(label="Lithium")
    mnO2 = core_models.ChemicalSubstance(label="Manganese dioxide")
    electrolyte = core_models.Electrolyte(
        label="LP57",
        hasSolvent=core_models.ChemicalSubstance(label="EC/EMC"),
        hasSolute=core_models.ChemicalSubstance(label="LiPF6"),
    )

    cell = core_models.factory.build_cr2032_cell(
        positive_electrode=core_models.factory.build_electrode(
            active_material=mnO2, label="Positive electrode"
        ),
        negative_electrode=core_models.factory.build_electrode(
            active_material=lithium, label="Negative electrode"
        ),
        electrolyte=electrolyte,
    )

    json_ld = cell.to_jsonld()

    assert json_ld["@type"] == "CR2032"
    assert json_ld["hasPositiveElectrode"]["hasActiveMaterial"]["label"] == "Manganese dioxide"
    assert json.loads(json.dumps(json_ld))  # ensure serializable
