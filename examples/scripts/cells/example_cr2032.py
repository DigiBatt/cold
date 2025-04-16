import cold  # <- imports your whole package properly
import json


# Instantiate data model
my_cr2032 = cold.CR2032()

# Assign properties
my_cr2032.hasProperty = [cold.NominalVoltage(3.2, "Volt")]

# Serialize to JSON-LD
json_ld = my_cr2032.to_jsonld()
print(json.dumps(json_ld, indent=4))
