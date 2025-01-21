
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class ChromiumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `ChromiumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_88748886_9b7c_4df0_91eb_fe91ecc1b9cd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChromiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChromiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_88748886_9b7c_4df0_91eb_fe91ecc1b9cd',
    
    class_name='ChromiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_88748886_9b7c_4df0_91eb_fe91ecc1b9cd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChromiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    