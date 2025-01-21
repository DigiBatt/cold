
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalModule import Electrochemical



from .ElectrochemicalTestingProcedureModule import ElectrochemicalTestingProcedure





from .TaskModule import Task





class CyclingTest(Electrochemical, ElectrochemicalTestingProcedure):
    """
    Class representing the `CyclingTest` entity, which inherits from:
    - Electrochemical, ElectrochemicalTestingProcedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_435b22d4_c441_45ea_8c79_0cbec11fd287'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CyclingTest'`
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
    obj = CyclingTest(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_435b22d4_c441_45ea_8c79_0cbec11fd287',
    
    class_name='CyclingTest',
    
    elucidation="example_value",
    
    hasTask="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_435b22d4_c441_45ea_8c79_0cbec11fd287',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CyclingTest',
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
    
    

    

    