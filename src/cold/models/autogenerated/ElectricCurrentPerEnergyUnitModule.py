
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class ElectricCurrentPerEnergyUnit(SIDimensionalUnit):
    """
    Class representing the `ElectricCurrentPerEnergyUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_53b10105_52c7_4746_ab73_a5a30bd198e2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentPerEnergyUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentPerEnergyUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_53b10105_52c7_4746_ab73_a5a30bd198e2',
    
    class_name='ElectricCurrentPerEnergyUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_53b10105_52c7_4746_ab73_a5a30bd198e2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentPerEnergyUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    