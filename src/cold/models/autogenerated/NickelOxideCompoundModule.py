
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class NickelOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `NickelOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_b8c65e71_05de_4f07_acd8_a16938b550fd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NickelOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NickelOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_b8c65e71_05de_4f07_acd8_a16938b550fd',
    
    class_name='NickelOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_b8c65e71_05de_4f07_acd8_a16938b550fd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NickelOxideCompound',
        alias="class_name"
    )
    

    
    

    

    