
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class PowerPerAreaVolumeUnit(SIDimensionalUnit):
    """
    Class representing the `PowerPerAreaVolumeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_36e03182_1be9_497c_bb71_e26fbb9160d2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PowerPerAreaVolumeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PowerPerAreaVolumeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_36e03182_1be9_497c_bb71_e26fbb9160d2',
    
    class_name='PowerPerAreaVolumeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_36e03182_1be9_497c_bb71_e26fbb9160d2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PowerPerAreaVolumeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    