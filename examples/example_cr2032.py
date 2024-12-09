import sys
import os

from cold.models import autogenerated as cold
from pydantic import ValidationError
import json

try:

    my_cr2032 = cold.CR2032()

    # Serialize to JSON-LD
    json_ld = my_cr2032.to_jsonld()
    print(json.dumps(json_ld, indent=4))


except ValidationError as e:
    print("ValidationError:")
    print(e.json())
