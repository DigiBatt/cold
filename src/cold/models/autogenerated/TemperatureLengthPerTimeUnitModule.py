
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class TemperatureLengthPerTimeUnit(SIDimensionalUnit):
    """
    Class representing the `TemperatureLengthPerTimeUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0d4bdfcd_f4f0_4b8f_b470_e3f654e37d33'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemperatureLengthPerTimeUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemperatureLengthPerTimeUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_0d4bdfcd_f4f0_4b8f_b470_e3f654e37d33',
    
    class_name='TemperatureLengthPerTimeUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0d4bdfcd_f4f0_4b8f_b470_e3f654e37d33',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemperatureLengthPerTimeUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    