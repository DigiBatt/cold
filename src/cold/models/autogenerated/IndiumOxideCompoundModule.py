
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PostTransitionMetalOxideCompoundModule import PostTransitionMetalOxideCompound







class IndiumOxideCompound(PostTransitionMetalOxideCompound):
    """
    Class representing the `IndiumOxideCompound` entity, which inherits from:
    - PostTransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_8f1af9c2_9b6d_44f4_8f55_70a4cd5f9dde'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IndiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IndiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_8f1af9c2_9b6d_44f4_8f55_70a4cd5f9dde',
    
    class_name='IndiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_8f1af9c2_9b6d_44f4_8f55_70a4cd5f9dde',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IndiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    