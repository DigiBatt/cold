
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LithiumSaltCompoundModule import LithiumSaltCompound







class LithiumBisoxalatophosphate(LithiumSaltCompound):
    """
    Class representing the `LithiumBisoxalatophosphate` entity, which inherits from:
    - LithiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_6cdc8512_d4f2_4904_8471_3121871d48e8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumBisoxalatophosphate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumBisoxalatophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_6cdc8512_d4f2_4904_8471_3121871d48e8',
    
    class_name='LithiumBisoxalatophosphate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_6cdc8512_d4f2_4904_8471_3121871d48e8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumBisoxalatophosphate',
        alias="class_name"
    )
    

    
    

    

    