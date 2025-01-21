
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InorganicCompoundModule import InorganicCompound







class MixedMetalOxideCompound(InorganicCompound):
    """
    Class representing the `MixedMetalOxideCompound` entity, which inherits from:
    - InorganicCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_15d08ff9_7685_4020_8481_d9c9b0052176'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MixedMetalOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MixedMetalOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_15d08ff9_7685_4020_8481_d9c9b0052176',
    
    class_name='MixedMetalOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_15d08ff9_7685_4020_8481_d9c9b0052176',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MixedMetalOxideCompound',
        alias="class_name"
    )
    

    
    

    

    