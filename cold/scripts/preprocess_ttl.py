import os
import sys
from rdflib import Graph, RDF, RDFS, OWL, URIRef

import sys
import os
from pathlib import Path

# Base directory = project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Ensure VSCode-friendly relative imports always work
sys.path.insert(0, str(BASE_DIR))

# Paths
INPUT_FILE = BASE_DIR / 'models' / 'ontology' / 'files' / 'originals' / 'emmo_battery.ttl'
OUTPUT_FILE = BASE_DIR / 'models' / 'ontology' / 'files' / 'formatted' / 'emmo_battery_tree.ttl'



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


def main():
    print("Loading graph...")
    g = load_graph(INPUT_FILE)

    print("Finding and removing circular dependencies on any object property...")
    removed = find_and_remove_cycles(g)

    print(f"Removed {removed} problematic triples.")

    print(f"Saving cleaned TTL to {OUTPUT_FILE}")
    g.serialize(destination=OUTPUT_FILE, format="turtle")


if __name__ == "__main__":
    main()
