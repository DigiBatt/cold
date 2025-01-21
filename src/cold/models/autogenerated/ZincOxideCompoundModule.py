
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class ZincOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `ZincOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_28754642_a1ed_4f39_8b00_2c7857336bab'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_28754642_a1ed_4f39_8b00_2c7857336bab',
    
    class_name='ZincOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_28754642_a1ed_4f39_8b00_2c7857336bab',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincOxideCompound',
        alias="class_name"
    )
    

    
    

    

    