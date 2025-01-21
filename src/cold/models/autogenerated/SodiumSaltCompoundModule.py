
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkaliMetalSaltCompoundModule import AlkaliMetalSaltCompound







class SodiumSaltCompound(AlkaliMetalSaltCompound):
    """
    Class representing the `SodiumSaltCompound` entity, which inherits from:
    - AlkaliMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_584bfc73_2715_417f_973c_552ae58529f5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_584bfc73_2715_417f_973c_552ae58529f5',
    
    class_name='SodiumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_584bfc73_2715_417f_973c_552ae58529f5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    