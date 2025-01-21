
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class IronOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `IronOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_52da9471_9979_44b0_a415_63c72110fd43'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IronOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IronOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_52da9471_9979_44b0_a415_63c72110fd43',
    
    class_name='IronOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_52da9471_9979_44b0_a415_63c72110fd43',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IronOxideCompound',
        alias="class_name"
    )
    

    
    

    

    