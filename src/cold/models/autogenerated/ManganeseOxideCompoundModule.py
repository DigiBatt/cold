
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class ManganeseOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `ManganeseOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_5a4d05f1_dd15_465b_8b44_704238e20813'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ManganeseOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ManganeseOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_5a4d05f1_dd15_465b_8b44_704238e20813',
    
    class_name='ManganeseOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_5a4d05f1_dd15_465b_8b44_704238e20813',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ManganeseOxideCompound',
        alias="class_name"
    )
    

    
    

    

    