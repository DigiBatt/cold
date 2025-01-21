
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InorganicCompoundModule import InorganicCompound







class TransitionMetalOxideCompound(InorganicCompound):
    """
    Class representing the `TransitionMetalOxideCompound` entity, which inherits from:
    - InorganicCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_b474f792_011e_4c9a_8dee_b99d6459cd66'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransitionMetalOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TransitionMetalOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_b474f792_011e_4c9a_8dee_b99d6459cd66',
    
    class_name='TransitionMetalOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_b474f792_011e_4c9a_8dee_b99d6459cd66',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransitionMetalOxideCompound',
        alias="class_name"
    )
    

    
    

    

    