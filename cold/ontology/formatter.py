from rdflib import Graph, Namespace, RDF, RDFS, SKOS, OWL, Literal, BNode, URIRef


def get_fragment(uri):
    """Extract the fragment from a URI (after # or last /)."""
    return uri.split("#")[-1] if "#" in uri else uri.rsplit("/", 1)[-1]


def load_graph(filepath):
    g = Graph()
    g.parse(filepath, format="turtle")
    return g


def get_superclasses(graph, cls):
    """Recursively get all superclasses of a class"""
    supers = set()
    queue = [cls]
    while queue:
        current = queue.pop()
        for s in graph.objects(current, RDFS.subClassOf):
            if isinstance(s, URIRef) and s not in supers:
                supers.add(s)
                queue.append(s)
    return supers


def find_and_remove_cycles(graph):
    """Detect and remove circular subclass relations caused by owl:Restrictions."""
    to_remove = []

    for s in graph.subjects(RDFS.subClassOf, None):
        for restriction in graph.objects(s, RDFS.subClassOf):
            if (restriction, RDF.type, OWL.Restriction) not in graph:
                continue

            prop = graph.value(restriction, OWL.onProperty)
            target = graph.value(restriction, OWL.someValuesFrom)

            if not (prop and target):
                continue

            supers = get_superclasses(graph, target)

            if s in supers:
                print(f"Detected circular dependency via property {prop}")
                print(f"→ {s} --[{prop}]--> {target} subclassOf* {s}")
                to_remove.append((s, RDFS.subClassOf, restriction))

    for triple in to_remove:
        print(f"Removing triple: {triple}")
        graph.remove(triple)

    return len(to_remove)


def enforce_single_inheritance(graph):
    """Ensure each class has only one non-restriction parent."""
    to_remove = []

    for cls in set(graph.subjects(RDF.type, OWL.Class)):
        parents = list(graph.objects(cls, RDFS.subClassOf))

        # Keep restrictions
        real_parents = [
            p for p in parents
            if isinstance(p, URIRef) and (p, RDF.type, OWL.Class) in graph
        ]

        if len(real_parents) > 1:
            print(f"⚠️  Enforcing single inheritance: {cls} has multiple parents: {real_parents}")
            for bad_parent in real_parents[1:]:
                print(f"→ Removing: {cls} subClassOf {bad_parent}")
                to_remove.append((cls, RDFS.subClassOf, bad_parent))

    for triple in to_remove:
        graph.remove(triple)

    return len(to_remove)


def format_ontology(input_turtle, output_turtle):
    """Clean and normalize Turtle ontology for safe Pydantic class generation."""
    g = load_graph(input_turtle)

    SCHEMA = Namespace("https://schema.org/")
    SKOSNS = Namespace("http://www.w3.org/2004/02/skos/core#")
    OWLNS = Namespace("http://www.w3.org/2002/07/owl#")

    updated = Graph()
    updated.bind("schema", SCHEMA)
    updated.bind("skos", SKOSNS)
    updated.bind("owl", OWLNS)
    updated.bind("rdfs", RDFS)
    updated.bind("rdf", RDF)

    property_domains = {}
    property_ranges = {}

    for s, p, o in g:
        if (p, o) == (RDF.type, RDFS.Class):
            updated.add((s, RDF.type, OWLNS.Class))
        elif (p, o) == (RDF.type, RDF.Property):
            updated.add((s, RDF.type, OWLNS.ObjectProperty))
        elif p == RDFS.label:
            updated.add((s, SKOSNS.prefLabel, o))
        elif str(p) == "https://schema.org/domainIncludes":
            updated.add((s, RDFS.domain, o))
            property_domains.setdefault(s, set()).add(o)
        elif str(p) == "https://schema.org/rangeIncludes":
            updated.add((s, RDFS.range, o))
            property_ranges.setdefault(s, set()).add(o)
        else:
            updated.add((s, p, o))

    for prop, domains in property_domains.items():
        ranges = property_ranges.get(prop, [])
        for d in domains:
            for r in ranges:
                restriction = BNode()
                updated.add((d, RDFS.subClassOf, restriction))
                updated.add((restriction, RDF.type, OWLNS.Restriction))
                updated.add((restriction, OWLNS.onProperty, prop))
                updated.add((restriction, OWLNS.someValuesFrom, r))

    for s in set(updated.subjects()):
        if any(p in [RDFS.label, SKOSNS.prefLabel] for p in updated.predicates(subject=s)):
            continue
        if (s, RDF.type, OWLNS.Class) in updated or (s, RDF.type, OWLNS.ObjectProperty) in updated:
            updated.add((s, SKOSNS.prefLabel, Literal(get_fragment(str(s)))))

    print("Removing circular imports from restrictions...")
    cycles_removed = find_and_remove_cycles(updated)
    print(f"→ Removed {cycles_removed} triples.")

    print("Enforcing single inheritance to prevent MRO issues...")
    mro_removed = enforce_single_inheritance(updated)
    print(f"→ Removed {mro_removed} subclass relations.")

    updated.serialize(destination=output_turtle, format="turtle")
    print(f"Turtle file saved to: {output_turtle}")
