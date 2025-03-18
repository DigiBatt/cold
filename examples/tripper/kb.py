"""
"""
from pathlib import Path
import json

from tripper import Session, Triplestore
from tripper.datadoc import save_dict, search_iris
from tripper.datadoc.dataset import get_prefixes


thisdir = Path(__file__).resolve().parent


#ts = Triplestore(backend="rdflib")

session = Session()
ts = session.get_triplestore("FusekiTest")

# Issue - the ontology on github pages should be squashed
ELC = ts.bind(
    "elc",
    "https://w3id.org/emmo/domain/electrochemistry#",
    label_annotations=True,
    check=True,
)

# Att prefixes from source (not done transparently (yet) by json-ld format...)
ts.namespaces.update(
    get_prefixes(
        [
            "https://w3id.org/emmo/domain/battery/context",
            {
                "dc": "http://purl.org/dc/terms/",
                "ex": "http://example.com/data#",
            }
        ]
    )
)



ts.parse(thisdir / "cr2032.json", format="json-ld")

print(ts.serialize())
print("="*60)


# Find all resources who's description matches a regex
print()
print("Description matches '^A table':")
print(search_iris(ts, regex={"description": "^A table"}))

# Find all resources who's description matches a regex
print()
print("Resources provided by Sridevi:")
print(search_iris(ts, regex={"dc:provider.dc:name": "Sridevi Krishnamurthi"}))
