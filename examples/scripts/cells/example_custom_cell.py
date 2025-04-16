import cold  # <- imports your whole package properly
import cold.utils.helpers as helpers
import json

# Define the Bill of Materials
lithium = helpers.merge_models(cold.Lithium, cold.Foil)()
mno2 = helpers.merge_models(cold.ManganeseDioxide, cold.Powder)()
ec = cold.EthyleneCarbonate()
emc = cold.EthylMethylCarbonate()
lipf6 = cold.LithiumHexafluorophosphate()
solvent = cold.Mixture(hasConstituent=[ec, emc])
lp57 = cold.Solution(hasSolvent = solvent, hasSolute=lipf6)

# Define material properties
ec.hasProperty = [cold.MassFraction(0.3, "UnitOne")]
emc.hasProperty = [cold.MassFraction(0.7, "UnitOne")]    
lipf6.hasProperty = [cold.MassFraction(0.127, "UnitOne")]

# Build electrodes
ne = cold.Electrode(hasActiveMaterial = lithium)
pe = cold.Electrode(hasActiveMaterial = mno2)

# Define case
case = cold.CoinCase()
case.hasProperty = [
    cold.Diameter(20, "MilliMetre"),
    cold.Thickness(3.2, "MilliMetre")
]   

# Build cell
cell = cold.BatteryCell()
cell.hasCase = case
cell.hasPositiveElectrode = pe
cell.hasNegativeElectrode = ne
cell.hasElectrolyte = lp57

# Serialize to JSON-LD
json_ld = cell.to_jsonld()
print(json.dumps(json_ld, indent=4))

