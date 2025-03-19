from owlready2 import *

# Load the ontology from the local file
schema_org_ontology = get_ontology("https://schema.org/version/latest/schemaorg-current-https.ttl").load()

# Print ontology information
print(f"Ontology IRI: {schema_org_ontology.base_iri}")
print(f"Classes in ontology: {list(schema_org_ontology.classes())}")
