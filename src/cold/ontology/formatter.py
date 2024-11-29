from rdflib import Graph, Namespace, RDF, RDFS, SKOS, OWL


def format_ontology_ttl(input_turtle, output_turtle):
    """
    Updates a Turtle file by changing all `:class` prefixes to `owl`
    and replacing `rdfs:label` with `skos:prefLabel`.

    Args:
        input_turtle (str): Path to the input Turtle file.
        output_turtle (str): Path to the output Turtle file.
    """
    # Load the RDF graph
    g = Graph()
    g.parse(input_turtle, format="turtle")

    # Define namespaces
    SCHEMA = Namespace("https://schema.org/")
    SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

    # Iterate over each triple and apply transformations
    updated_graph = Graph()
    updated_graph.bind("schema", SCHEMA)
    updated_graph.bind("skos", SKOS)
    updated_graph.bind("owl", OWL)

    for subj, pred, obj in g:
        # Change `rdf:type rdfs:Class` to `rdf:type owl:Class`
        if pred == RDF.type and obj == RDFS.Class:
            updated_graph.add((subj, pred, OWL.Class))
        # Change `rdfs:label` to `skos:prefLabel`
        elif pred == RDFS.label:
            updated_graph.add((subj, SKOS.prefLabel, obj))
        # Copy other triples as-is
        else:
            updated_graph.add((subj, pred, obj))

    # Serialize the updated graph back to a Turtle file
    updated_graph.serialize(destination=output_turtle, format="turtle")
    print(f"Updated Turtle file saved to: {output_turtle}")
