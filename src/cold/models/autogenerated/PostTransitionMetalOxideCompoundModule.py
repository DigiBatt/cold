
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InorganicCompoundModule import InorganicCompound







class PostTransitionMetalOxideCompound(InorganicCompound):
    """
    Class representing the `PostTransitionMetalOxideCompound` entity, which inherits from:
    - InorganicCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_61c88366_7689_4814_b0c5_1f53aef1eebd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PostTransitionMetalOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PostTransitionMetalOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_61c88366_7689_4814_b0c5_1f53aef1eebd',
    
    class_name='PostTransitionMetalOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_61c88366_7689_4814_b0c5_1f53aef1eebd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PostTransitionMetalOxideCompound',
        alias="class_name"
    )
    

    
    

    

    