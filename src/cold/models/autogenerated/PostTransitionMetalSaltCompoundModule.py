
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SaltModule import Salt







class PostTransitionMetalSaltCompound(Salt):
    """
    Class representing the `PostTransitionMetalSaltCompound` entity, which inherits from:
    - Salt

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_8c40be1f_0931_4db9_832f_cb63556f6a5a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PostTransitionMetalSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PostTransitionMetalSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_8c40be1f_0931_4db9_832f_cb63556f6a5a',
    
    class_name='PostTransitionMetalSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_8c40be1f_0931_4db9_832f_cb63556f6a5a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PostTransitionMetalSaltCompound',
        alias="class_name"
    )
    

    
    

    

    