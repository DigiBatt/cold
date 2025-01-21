
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class AreaTimeTemperatureUnit(SIDimensionalUnit):
    """
    Class representing the `AreaTimeTemperatureUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_48a3c106_9d39_455e_a849_81ceff95bdea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AreaTimeTemperatureUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AreaTimeTemperatureUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_48a3c106_9d39_455e_a849_81ceff95bdea',
    
    class_name='AreaTimeTemperatureUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_48a3c106_9d39_455e_a849_81ceff95bdea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AreaTimeTemperatureUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    