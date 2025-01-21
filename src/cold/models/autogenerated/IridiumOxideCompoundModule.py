
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class IridiumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `IridiumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_4ad18bbe_6478_4009_8f80_b669a6ae3f7a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IridiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IridiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_4ad18bbe_6478_4009_8f80_b669a6ae3f7a',
    
    class_name='IridiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_4ad18bbe_6478_4009_8f80_b669a6ae3f7a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IridiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    