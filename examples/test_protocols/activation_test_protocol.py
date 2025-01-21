import sys
import os

# Add the src/ directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(),"..", 'src')))
print(sys.path)

import cold.models.autogenerated as cold

from pydantic import ValidationError
import json

def activation_test_protocol():
    try:
        #1st step
        resting_0=cold.Resting()
        resting_0.hasProperty=[cold.Duration(0.6,"Hour")]
        #2st step
        charging_1=cold.ConstantCurrentCharging()
        chargingcrate_1=cold.ChargingCRate(1/10,"UnitOne")
        upper_v_limit=cold.UpperVoltageLimit(4.2,"Volt")
        charging_1.hasMeasurementParameter=[chargingcrate_1,upper_v_limit]
        #3nd step
        discharging_1=cold.ConstantCurrentDischarging()
        dischargingcrate_1=cold.DischargingCRate(1/10,"UnitOne")
        lower_v_limit=cold.UpperVoltageLimit(2.9,"Volt")
        discharging_1.hasMeasurementParameter=[dischargingcrate_1,lower_v_limit]
        #4rd step-loop
        iterative_workflow=cold.IterativeWorkflow()
        iterative_workflow.hasProperty=[cold.NumberOfIterations(2,"UnitOne")]
        iterative_workflow.hasTask=[charging_1]
        #5th step- charge
        charging_2=cold.ConstantCurrentCharging()
        chargingcrate_2=cold.ChargingCRate(1/50,"UnitOne")
        upper_v_limit=cold.UpperVoltageLimit(4.2,"Volt")
        charging_2.hasMeasurementParameter=[chargingcrate_2,upper_v_limit]
        #6th step- discharge
        discharging_2=cold.ConstantCurrentDischarging()
        dischargingcrate_2=cold.DischargingCRate(1/50,"UnitOne")
        lower_v_limit=cold.UpperVoltageLimit(2.9,"Volt")
        discharging_2.hasMeasurementParameter=[dischargingcrate_2,lower_v_limit]
        #7th step- charge
        charging_3=cold.ConstantCurrentCharging()
        chargingcrate_3=cold.ChargingCRate(1/10,"UnitOne")
        charging_3_time_limit=cold.Duration(6,"Hour")
        charging_1.hasMeasurementParameter=[chargingcrate_1,charging_3_time_limit]
        #8th step- EIS
        characterisation_step=cold.ElectrochemicalImpedanceSpectroscopy()
        lower_frequency_limit=cold.LowerFrequencyLimit(100*10^3,"Hertz")
        upper_frequency_limit=cold.UpperFrequencyLimit(100*10^6,"Hertz")
        voltage_limit=cold.VoltageLimit(10*10^-3,"Volt")
        characterisation_step.hasProperty=[lower_frequency_limit,upper_frequency_limit,voltage_limit]
        #9th step- charge
        charging_4=cold.ConstantCurrentCharging()
        chargingcrate_4=cold.ChargingCRate(1/10,"UnitOne")
        upper_v_limit=cold.UpperVoltageLimit(4.2,"Volt")
        charging_4.hasMeasurementParameter=[chargingcrate_4,upper_v_limit]
        #10th step-discharge
        discharging_5=cold.ConstantCurrentDischarging()
        dischargingcrate_5=cold.DischargingCRate(1/10,"UnitOne")
        lower_v_limit=cold.UpperVoltageLimit(2.9,"Volt")
        discharging_5.hasMeasurementParameter=[dischargingcrate_5,lower_v_limit]
        test_workflow=cold.SerialWorkflow()
        # iterative_workflow=cold.IterativeWorkflow()
        # resting=cold.Resting()
        # resting.hasProperty=[cold.Duration(1,"Hour")]
        test_workflow.hasTask=[resting_0,charging_1,discharging_1,iterative_workflow,charging_2,discharging_2,charging_3,characterisation_step,charging_4,discharging_5]
        json_ld = test_workflow.to_jsonld()
        # print(json.dumps(json_ld, indent=4))
        # print(type(json_ld))
        return json_ld
    except AttributeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    activation_test_protocol()
