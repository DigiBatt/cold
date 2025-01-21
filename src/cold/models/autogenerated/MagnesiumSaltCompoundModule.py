
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineEarthMetalSaltCompoundModule import AlkalineEarthMetalSaltCompound







class MagnesiumSaltCompound(AlkalineEarthMetalSaltCompound):
    """
    Class representing the `MagnesiumSaltCompound` entity, which inherits from:
    - AlkalineEarthMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0001e895_e74b_438f_b47f_b52f33d68331'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0001e895_e74b_438f_b47f_b52f33d68331',
    
    class_name='MagnesiumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0001e895_e74b_438f_b47f_b52f33d68331',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    