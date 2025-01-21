
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class VandaiumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `VandaiumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_a639df56_1fb2_47f3_8069_c929b5a84b86'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VandaiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VandaiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_a639df56_1fb2_47f3_8069_c929b5a84b86',
    
    class_name='VandaiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_a639df56_1fb2_47f3_8069_c929b5a84b86',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VandaiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    