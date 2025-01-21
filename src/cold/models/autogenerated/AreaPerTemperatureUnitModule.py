
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class AreaPerTemperatureUnit(SIDimensionalUnit):
    """
    Class representing the `AreaPerTemperatureUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_002e4002_58c7_4aea_ac1f_bba5188818ff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AreaPerTemperatureUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AreaPerTemperatureUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_002e4002_58c7_4aea_ac1f_bba5188818ff',
    
    class_name='AreaPerTemperatureUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_002e4002_58c7_4aea_ac1f_bba5188818ff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AreaPerTemperatureUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    