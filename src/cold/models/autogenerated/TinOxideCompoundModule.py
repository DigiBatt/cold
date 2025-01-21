
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class TinOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `TinOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_155e894b_66de_4cda_9dbe_adbeca7d8102'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TinOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TinOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_155e894b_66de_4cda_9dbe_adbeca7d8102',
    
    class_name='TinOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_155e894b_66de_4cda_9dbe_adbeca7d8102',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TinOxideCompound',
        alias="class_name"
    )
    

    
    

    

    