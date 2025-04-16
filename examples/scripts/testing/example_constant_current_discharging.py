import cold
import cold.utils.helpers as helpers
import json

# Instantiate the test
test = helpers.merge_models(cold.BatteryTest, cold.SerialWorkflow)()

# Define the steps
resting = cold.Resting()
discharging = cold.Discharging()

# Assign parameters to the steps
resting.hasInput = [cold.Duration(1, "Hour")]
resting.identifier = "id1"
discharging.hasInput = [
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
test.hasBeginTask = [resting]
resting.hasNext = [discharging]

# Serialize to JSON-LD
json_ld = test.to_jsonld()
print(json.dumps(json_ld, indent=4))

