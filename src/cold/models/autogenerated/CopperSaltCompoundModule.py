
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalSaltCompoundModule import TransitionMetalSaltCompound







class CopperSaltCompound(TransitionMetalSaltCompound):
    """
    Class representing the `CopperSaltCompound` entity, which inherits from:
    - TransitionMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_094f08bc_90ea_4118_b136_47e61e495ab5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CopperSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CopperSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_094f08bc_90ea_4118_b136_47e61e495ab5',
    
    class_name='CopperSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_094f08bc_90ea_4118_b136_47e61e495ab5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CopperSaltCompound',
        alias="class_name"
    )
    

    
    

    

    