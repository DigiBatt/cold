
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StringModule import String







class UserCase(String):
    """
    Class representing the `UserCase` entity, which inherits from:
    - String

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#UserCase'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UserCase'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UserCase(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#UserCase',
    
    class_name='UserCase',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#UserCase',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UserCase',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    