
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SerialWorkflowModule import SerialWorkflow





from .TaskModule import Task





class IterativeWorkflow(SerialWorkflow):
    """
    Class representing the `IterativeWorkflow` entity, which inherits from:
    - SerialWorkflow

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ddecfff6_d3a1_4972_b9e9_3d0ca11a3a0b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IterativeWorkflow'`
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
    obj = IterativeWorkflow(
    
    class_iri='https://w3id.org/emmo#EMMO_ddecfff6_d3a1_4972_b9e9_3d0ca11a3a0b',
    
    class_name='IterativeWorkflow',
    
    elucidation="example_value",
    
    hasTask="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ddecfff6_d3a1_4972_b9e9_3d0ca11a3a0b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IterativeWorkflow',
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
    
    

    

    