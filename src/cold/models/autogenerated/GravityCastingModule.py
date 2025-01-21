
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CastingModule import Casting







class GravityCasting(Casting):
    """
    Class representing the `GravityCasting` entity, which inherits from:
    - Casting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f1d0f28b_7575_4e82_8d22_cb5b46b84cfd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GravityCasting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GravityCasting(
    
    class_iri='https://w3id.org/emmo#EMMO_f1d0f28b_7575_4e82_8d22_cb5b46b84cfd',
    
    class_name='GravityCasting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f1d0f28b_7575_4e82_8d22_cb5b46b84cfd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GravityCasting',
        alias="class_name"
    )
    

    
    

    

    