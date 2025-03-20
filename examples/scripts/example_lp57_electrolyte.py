import sys
import os

# Add the directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
print(sys.path)

import cold.models.autogenerated as cold
import cold.utils.helpers as helpers
from pydantic import ValidationError
import json


# Define bill of materials
ec = cold.EthyleneCarbonate()    
emc = cold.EthylMethylCarbonate()    
lipf6 = cold.LithiumHexafluorophosphate()    

# Mix components
solvent = cold.Mixture(hasConstituent=[ec, emc])
lp57 = cold.Solution(hasSolvent = solvent, hasSolute=lipf6)

# Set properties
ec.hasProperty = [cold.MassFraction(0.3, "UnitOne")]
emc.hasProperty = [cold.MassFraction(0.7, "UnitOne")]
lipf6.hasProperty = [cold.MassFraction(0.127, "UnitOne")]

# Serialize to JSON-LD
json_ld = lp57.to_jsonld()
print(json.dumps(json_ld, indent=4))

