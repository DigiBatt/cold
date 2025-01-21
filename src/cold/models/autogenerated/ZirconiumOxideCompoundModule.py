
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class ZirconiumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `ZirconiumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_a9218f8f_2e80_497e_b968_b4947cf21802'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZirconiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZirconiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_a9218f8f_2e80_497e_b968_b4947cf21802',
    
    class_name='ZirconiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_a9218f8f_2e80_497e_b968_b4947cf21802',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZirconiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    