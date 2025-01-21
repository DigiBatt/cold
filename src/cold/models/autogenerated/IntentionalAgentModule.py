
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AgentModule import Agent







class IntentionalAgent(Agent):
    """
    Class representing the `IntentionalAgent` entity, which inherits from:
    - Agent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c130614a_2985_476d_a7ed_8a137847703c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IntentionalAgent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IntentionalAgent(
    
    class_iri='https://w3id.org/emmo#EMMO_c130614a_2985_476d_a7ed_8a137847703c',
    
    class_name='IntentionalAgent',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c130614a_2985_476d_a7ed_8a137847703c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IntentionalAgent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    