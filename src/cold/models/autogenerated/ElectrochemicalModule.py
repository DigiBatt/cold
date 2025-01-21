
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkflowModule import Workflow





from .ObjectModule import Object



from .TaskModule import Task





class Electrochemical(Workflow):
    """
    Class representing the `Electrochemical` entity, which inherits from:
    - Workflow

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Electrochemical'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electrochemical'`
        - **Alias**: `class_name`
    
    - `hasTemporaryParticipant` (`Optional[Object]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTemporaryParticipant`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasTask` (`Optional[Task]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTask`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Electrochemical(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#Electrochemical',
    
    class_name='Electrochemical',
    
    hasTemporaryParticipant="example_value",
    
    elucidation="example_value",
    
    hasTask="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#Electrochemical',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electrochemical',
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
    
    hasTask: Optional[Task] = Field(
        None,
        alias="hasTask"
    )
    

    
    @validator("hasTemporaryParticipant", pre=True, always=True)
    def validate_hasTemporaryParticipant(cls, value):
        if value is not None and not isinstance(value, Object):
            raise ValueError(f"Field 'hasTemporaryParticipant' must be an instance of 'Object' or its subclass.")
        return value
    
    @validator("hasTask", pre=True, always=True)
    def validate_hasTask(cls, value):
        if value is not None and not isinstance(value, Task):
            raise ValueError(f"Field 'hasTask' must be an instance of 'Task' or its subclass.")
        return value
    
    

    

    