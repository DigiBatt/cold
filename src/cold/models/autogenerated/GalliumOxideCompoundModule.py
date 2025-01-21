
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PostTransitionMetalOxideCompoundModule import PostTransitionMetalOxideCompound







class GalliumOxideCompound(PostTransitionMetalOxideCompound):
    """
    Class representing the `GalliumOxideCompound` entity, which inherits from:
    - PostTransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0111fe83_2d6c_4df0_9fd3_500ddda7242c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GalliumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GalliumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0111fe83_2d6c_4df0_9fd3_500ddda7242c',
    
    class_name='GalliumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0111fe83_2d6c_4df0_9fd3_500ddda7242c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GalliumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    