from ontopy import get_ontology

def load_ontology(url: str = "https://w3id.org/emmo/domain/battery/inferred"):
    """Load ontology from the given URL."""
    print(f"Loading ontology from {url}...")
    return get_ontology(url).load()
