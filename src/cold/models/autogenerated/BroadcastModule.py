
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MixedTilingModule import MixedTiling







class Broadcast(MixedTiling):
    """
    Class representing the `Broadcast` entity, which inherits from:
    - MixedTiling

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_79aad3fb_2e01_4626_8369_4e914893aa6d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Broadcast'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Broadcast(
    
    class_iri='https://w3id.org/emmo#EMMO_79aad3fb_2e01_4626_8369_4e914893aa6d',
    
    class_name='Broadcast',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_79aad3fb_2e01_4626_8369_4e914893aa6d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Broadcast',
        alias="class_name"
    )
    

    
    

    

    