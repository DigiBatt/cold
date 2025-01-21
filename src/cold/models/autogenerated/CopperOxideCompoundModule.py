
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class CopperOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `CopperOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_f7d13311_6dd1_422c_b32b_b55fd9e77145'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CopperOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CopperOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_f7d13311_6dd1_422c_b32b_b55fd9e77145',
    
    class_name='CopperOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_f7d13311_6dd1_422c_b32b_b55fd9e77145',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CopperOxideCompound',
        alias="class_name"
    )
    

    
    

    

    