
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkflowModule import Workflow



from .CyclingModule import Cycling





from .TaskModule import Task





class ConstantCurrentConstantVoltageCycling(Workflow, Cycling):
    """
    Class representing the `ConstantCurrentConstantVoltageCycling` entity, which inherits from:
    - Workflow, Cycling

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ac6c2371_995a_4fcb_89a2_15cb6615741e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantCurrentConstantVoltageCycling'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasTask` (`Optional[Task]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTask`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantCurrentConstantVoltageCycling(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ac6c2371_995a_4fcb_89a2_15cb6615741e',
    
    class_name='ConstantCurrentConstantVoltageCycling',
    
    elucidation="example_value",
    
    hasTask="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ac6c2371_995a_4fcb_89a2_15cb6615741e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantCurrentConstantVoltageCycling',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasTask: Optional[Task] = Field(
        None,
        alias="hasTask"
    )
    

    
    @validator("hasTask", pre=True, always=True)
    def validate_hasTask(cls, value):
        if value is not None and not isinstance(value, Task):
            raise ValueError(f"Field 'hasTask' must be an instance of 'Task' or its subclass.")
        return value
    
    

    

    