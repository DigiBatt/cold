
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class MercuryOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `MercuryOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_d9f73522_049b_4542_909d_d7daefa9613b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MercuryOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MercuryOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_d9f73522_049b_4542_909d_d7daefa9613b',
    
    class_name='MercuryOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_d9f73522_049b_4542_909d_d7daefa9613b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MercuryOxideCompound',
        alias="class_name"
    )
    

    
    

    

    