
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalSaltCompoundModule import TransitionMetalSaltCompound







class NickelSaltCompound(TransitionMetalSaltCompound):
    """
    Class representing the `NickelSaltCompound` entity, which inherits from:
    - TransitionMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_dce90b66_3414_4f5d_b818_4a0e4339e949'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NickelSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NickelSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_dce90b66_3414_4f5d_b818_4a0e4339e949',
    
    class_name='NickelSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_dce90b66_3414_4f5d_b818_4a0e4339e949',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NickelSaltCompound',
        alias="class_name"
    )
    

    
    

    

    