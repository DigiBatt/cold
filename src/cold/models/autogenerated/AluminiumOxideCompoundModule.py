
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PostTransitionMetalOxideCompoundModule import PostTransitionMetalOxideCompound







class AluminiumOxideCompound(PostTransitionMetalOxideCompound):
    """
    Class representing the `AluminiumOxideCompound` entity, which inherits from:
    - PostTransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_6411d319_81a0_40f3_8e4d_09784d1c7644'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AluminiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AluminiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_6411d319_81a0_40f3_8e4d_09784d1c7644',
    
    class_name='AluminiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_6411d319_81a0_40f3_8e4d_09784d1c7644',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AluminiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    