from cold.ontology.loader import load_ontology
from cold.ontology.extractor import extract_classes, extract_properties

def test_extract_classes():
    ontology = load_ontology()
    classes = extract_classes(ontology)
    assert len(classes) > 0, "No classes extracted from the ontology"

def test_extract_properties():
    ontology = load_ontology()
    classes = extract_classes(ontology, max_classes=1)
    properties, dependencies = extract_properties(classes[0])
    assert isinstance(properties, list), "Properties should be a list"
    assert isinstance(dependencies, list), "Dependencies should be a list"
