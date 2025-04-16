import cold
import cold.utils.helpers as helpers
from pydantic import ValidationError
import json

# Instantiate the test
test = helpers.merge_models(cold.BatteryTest, cold.IterativeWorkflow)()

# Define the steps
resting = cold.Resting()
discharging = cold.ConstantCurrentDischarging()

# Assign parameters to the steps
resting.hasProcessParameter = cold.Duration(1, "Hour")
resting.identifier = "id1"
discharging.hasProcessParameter = [
    cold.DischargingCRate(1, "AmperePerAmpereHour"),
    cold.LowerVoltageLimit(3, "Volt")
]
discharging.identifier = "id2"

# Compile the tasks as a list
test.hasTask = [
    resting, 
    discharging
]

# Put the tasks in order
test.hasBeginTask = resting
resting.hasNext = discharging

# Serialize to JSON-LD
json_ld = test.to_jsonld()
print(json.dumps(json_ld, indent=4))

