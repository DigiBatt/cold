import cold  # <- imports your whole package properly
import cold.utils.helpers as helpers
import json

# Create a new dedicated class
my_dataset = cold.Thing()

# Serialize to JSON-LD
json_ld = my_dataset.to_jsonld()
print(json.dumps(json_ld, indent=4))
print(my_dataset)
