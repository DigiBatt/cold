
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalSaltCompoundModule import TransitionMetalSaltCompound







class CobaltSaltCompound(TransitionMetalSaltCompound):
    """
    Class representing the `CobaltSaltCompound` entity, which inherits from:
    - TransitionMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_bc76f17d_931a_4728_9663_9f8ed208d5e4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CobaltSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CobaltSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_bc76f17d_931a_4728_9663_9f8ed208d5e4',
    
    class_name='CobaltSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_bc76f17d_931a_4728_9663_9f8ed208d5e4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CobaltSaltCompound',
        alias="class_name"
    )
    

    
    

    

    