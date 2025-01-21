
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class TemperatureMassPerAreaUnit(SIDimensionalUnit):
    """
    Class representing the `TemperatureMassPerAreaUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6726fbb8_c40a_4b55_a2d5_bf49352d1e73'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemperatureMassPerAreaUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemperatureMassPerAreaUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_6726fbb8_c40a_4b55_a2d5_bf49352d1e73',
    
    class_name='TemperatureMassPerAreaUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6726fbb8_c40a_4b55_a2d5_bf49352d1e73',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemperatureMassPerAreaUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    