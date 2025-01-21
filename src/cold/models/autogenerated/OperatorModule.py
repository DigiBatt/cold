
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PersonModule import Person



from .IntentionalAgentModule import IntentionalAgent







class Operator(Person, IntentionalAgent):
    """
    Class representing the `Operator` entity, which inherits from:
    - Person, IntentionalAgent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Operator'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Operator'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Operator(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Operator',
    
    class_name='Operator',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Operator',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Operator',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    