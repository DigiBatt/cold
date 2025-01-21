
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class PlatinumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `PlatinumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_2e4767fb_2c1b_43e5_9716_acd3f34b4301'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PlatinumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PlatinumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_2e4767fb_2c1b_43e5_9716_acd3f34b4301',
    
    class_name='PlatinumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_2e4767fb_2c1b_43e5_9716_acd3f34b4301',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PlatinumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    