
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricCurrentPerUnitEnergyUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricCurrentPerUnitEnergyUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1aaaceb6_c5eb_4cf3_a494_f82d43fda10a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentPerUnitEnergyUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentPerUnitEnergyUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_1aaaceb6_c5eb_4cf3_a494_f82d43fda10a',
    
    class_name='ElectricCurrentPerUnitEnergyUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1aaaceb6_c5eb_4cf3_a494_f82d43fda10a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentPerUnitEnergyUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    