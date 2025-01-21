
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class RhodiumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `RhodiumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_c7bab57c_23c4_41d7_b2dc_497683fc82db'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RhodiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RhodiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_c7bab57c_23c4_41d7_b2dc_497683fc82db',
    
    class_name='RhodiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_c7bab57c_23c4_41d7_b2dc_497683fc82db',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RhodiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    