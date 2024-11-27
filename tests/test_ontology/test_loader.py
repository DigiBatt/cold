from cold.ontology.loader import load_ontology

def test_load_ontology():
    ontology = load_ontology()
    assert ontology is not None, "Failed to load ontology"
    assert hasattr(ontology, "classes"), "Ontology does not contain classes"
