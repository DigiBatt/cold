
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineEarthMetalSaltCompoundModule import AlkalineEarthMetalSaltCompound







class CalciumSaltCompound(AlkalineEarthMetalSaltCompound):
    """
    Class representing the `CalciumSaltCompound` entity, which inherits from:
    - AlkalineEarthMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_c12c3203_9d18_4a69_8a10_25b100ff48c8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_c12c3203_9d18_4a69_8a10_25b100ff48c8',
    
    class_name='CalciumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_c12c3203_9d18_4a69_8a10_25b100ff48c8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    