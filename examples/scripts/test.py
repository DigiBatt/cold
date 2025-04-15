import cold  # <- imports your whole package properly
import cold.utils.helpers as helpers
from pydantic import ValidationError
import json

product = cold.ManufacturedProduct()
simon = cold.Person()
product.creator = "Simon"

print(product)

json_ld = product.to_jsonld()
print(json.dumps(json_ld, indent=4))

print(cold.Thickness.mro())