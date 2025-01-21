
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineEarthMetalSaltCompoundModule import AlkalineEarthMetalSaltCompound







class BariumSaltCompound(AlkalineEarthMetalSaltCompound):
    """
    Class representing the `BariumSaltCompound` entity, which inherits from:
    - AlkalineEarthMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_7dd5ebb3_1084_485a_9fbf_05954cd2da84'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_7dd5ebb3_1084_485a_9fbf_05954cd2da84',
    
    class_name='BariumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_7dd5ebb3_1084_485a_9fbf_05954cd2da84',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    