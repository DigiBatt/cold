
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalSaltCompoundModule import TransitionMetalSaltCompound







class IridiumSaltCompound(TransitionMetalSaltCompound):
    """
    Class representing the `IridiumSaltCompound` entity, which inherits from:
    - TransitionMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_63788521_5764_4ee2_8d8a_ce4978682546'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IridiumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IridiumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_63788521_5764_4ee2_8d8a_ce4978682546',
    
    class_name='IridiumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_63788521_5764_4ee2_8d8a_ce4978682546',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IridiumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    