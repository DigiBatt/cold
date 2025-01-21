
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectivePropertyModule import ObjectiveProperty







class ControlProperty(ObjectiveProperty):
    """
    Class representing the `ControlProperty` entity, which inherits from:
    - ObjectiveProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_33e6986c_b35a_4cae_9a94_acb23248065c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ControlProperty'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ControlProperty(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_33e6986c_b35a_4cae_9a94_acb23248065c',
    
    class_name='ControlProperty',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_33e6986c_b35a_4cae_9a94_acb23248065c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ControlProperty',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    