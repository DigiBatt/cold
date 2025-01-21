
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class PalladiumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `PalladiumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0dcf209c_6455_4305_9714_fec548742c6a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PalladiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PalladiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0dcf209c_6455_4305_9714_fec548742c6a',
    
    class_name='PalladiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0dcf209c_6455_4305_9714_fec548742c6a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PalladiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    