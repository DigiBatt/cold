from rdflib import Graph, Namespace, RDF, RDFS, SKOS, OWL, Literal, BNode
from urllib.parse import urlparse

def get_fragment(uri):
    """Extract the fragment from a URI (after # or last /)."""
    return uri.split("#")[-1] if "#" in uri else uri.rsplit("/", 1)[-1]

def format_ontology(input_turtle, output_turtle):
    """
    Normalize a Turtle file to align with EMMO-style conventions:
    - Promote rdfs:Class → owl:Class
    - Promote rdf:Property → owl:ObjectProperty
    - Replace rdfs:label → skos:prefLabel
    - Convert schema:domainIncludes → rdfs:domain
    - Convert schema:rangeIncludes → rdfs:range
    - Add skos:prefLabel based on IRI if missing
    - Add owl:Restriction axioms linking properties to classes via rdfs:subClassOf
    """
    g = Graph()
    g.parse(input_turtle, format="turtle")

    SCHEMA = Namespace("https://schema.org/")
    SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
    OWLNS = Namespace("http://www.w3.org/2002/07/owl#")

    updated_graph = Graph()
    updated_graph.bind("schema", SCHEMA)
    updated_graph.bind("skos", SKOS)
    updated_graph.bind("owl", OWLNS)
    updated_graph.bind("rdfs", RDFS)
    updated_graph.bind("rdf", RDF)

    # Map to store domain and range triples temporarily
    property_domains = {}
    property_ranges = {}

    # First pass: Normalize and collect schema.org-style domain/range
    for subj, pred, obj in g:
        if pred == RDF.type and obj == RDFS.Class:
            updated_graph.add((subj, RDF.type, OWLNS.Class))
        elif pred == RDF.type and obj == RDF.Property:
            updated_graph.add((subj, RDF.type, OWLNS.ObjectProperty))
        elif pred == RDFS.label:
            updated_graph.add((subj, SKOS.prefLabel, obj))
        elif str(pred) == "https://schema.org/domainIncludes":
            updated_graph.add((subj, RDFS.domain, obj))
            property_domains.setdefault(subj, set()).add(obj)
        elif str(pred) == "https://schema.org/rangeIncludes":
            updated_graph.add((subj, RDFS.range, obj))
            property_ranges.setdefault(subj, set()).add(obj)
        else:
            updated_graph.add((subj, pred, obj))

    # Add owl:Restrictions for each domain/range pair
    for prop, domains in property_domains.items():
        ranges = property_ranges.get(prop, [])
        for domain in domains:
            for range_ in ranges:
                restriction = BNode()
                updated_graph.add((domain, RDFS.subClassOf, restriction))
                updated_graph.add((restriction, RDF.type, OWLNS.Restriction))
                updated_graph.add((restriction, OWLNS.onProperty, prop))
                updated_graph.add((restriction, OWLNS.someValuesFrom, range_))

    # Add missing skos:prefLabel
    for subj in set(updated_graph.subjects()):
        has_label = any(pred in [RDFS.label, SKOS.prefLabel] for pred in updated_graph.predicates(subject=subj))
        is_class_or_prop = (
            (subj, RDF.type, OWLNS.Class) in updated_graph or
            (subj, RDF.type, OWLNS.ObjectProperty) in updated_graph
        )
        if is_class_or_prop and not has_label:
            label = get_fragment(str(subj))
            updated_graph.add((subj, SKOS.prefLabel, Literal(label)))

    updated_graph.serialize(destination=output_turtle, format="turtle")
    print(f"Updated Turtle file saved to: {output_turtle}")
