
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalSaltCompoundModule import TransitionMetalSaltCompound







class ManganeseSaltCompound(TransitionMetalSaltCompound):
    """
    Class representing the `ManganeseSaltCompound` entity, which inherits from:
    - TransitionMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_cb6d2c65_9977_4bb1_987a_5ea828de445f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ManganeseSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ManganeseSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_cb6d2c65_9977_4bb1_987a_5ea828de445f',
    
    class_name='ManganeseSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_cb6d2c65_9977_4bb1_987a_5ea828de445f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ManganeseSaltCompound',
        alias="class_name"
    )
    

    
    

    

    