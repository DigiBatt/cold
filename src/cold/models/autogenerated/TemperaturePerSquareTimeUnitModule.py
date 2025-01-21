
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class TemperaturePerSquareTimeUnit(SIDimensionalUnit):
    """
    Class representing the `TemperaturePerSquareTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c7188d13_52e6_43f7_9b6d_aba4c161fa8f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemperaturePerSquareTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemperaturePerSquareTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_c7188d13_52e6_43f7_9b6d_aba4c161fa8f',
    
    class_name='TemperaturePerSquareTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c7188d13_52e6_43f7_9b6d_aba4c161fa8f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemperaturePerSquareTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    