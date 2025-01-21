
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationWorkflowModule import CharacterisationWorkflow



from .CurrentControlledProcessModule import CurrentControlledProcess



from .CyclingModule import Cycling





from .TaskModule import Task





class GalvanostaticCycling(CharacterisationWorkflow, CurrentControlledProcess, Cycling):
    """
    Class representing the `GalvanostaticCycling` entity, which inherits from:
    - CharacterisationWorkflow, CurrentControlledProcess, Cycling

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79a8802e_8296_459a_b65d_6e5c79e1bf37'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GalvanostaticCycling'`
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
    obj = GalvanostaticCycling(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79a8802e_8296_459a_b65d_6e5c79e1bf37',
    
    class_name='GalvanostaticCycling',
    
    elucidation="example_value",
    
    hasTask="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79a8802e_8296_459a_b65d_6e5c79e1bf37',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GalvanostaticCycling',
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
    
    

    

    