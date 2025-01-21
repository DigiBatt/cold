
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentControlledProcessModule import CurrentControlledProcess





from .ObjectModule import Object





class CurrentHold(CurrentControlledProcess):
    """
    Class representing the `CurrentHold` entity, which inherits from:
    - CurrentControlledProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_78a8f60b_10c2_41ee_9946_d35437e1edb5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentHold'`
        - **Alias**: `class_name`
    
    - `hasTemporaryParticipant` (`Optional[Object]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTemporaryParticipant`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CurrentHold(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_78a8f60b_10c2_41ee_9946_d35437e1edb5',
    
    class_name='CurrentHold',
    
    hasTemporaryParticipant="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_78a8f60b_10c2_41ee_9946_d35437e1edb5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentHold',
        alias="class_name"
    )
    
    hasTemporaryParticipant: Optional[Object] = Field(
        None,
        alias="hasTemporaryParticipant"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasTemporaryParticipant", pre=True, always=True)
    def validate_hasTemporaryParticipant(cls, value):
        if value is not None and not isinstance(value, Object):
            raise ValueError(f"Field 'hasTemporaryParticipant' must be an instance of 'Object' or its subclass.")
        return value
    
    

    

    