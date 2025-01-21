
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CapacityModule import Capacity







class StepCapacity(Capacity):
    """
    Class representing the `StepCapacity` entity, which inherits from:
    - Capacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae108db7_8765_4329_9908_059277dee586'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StepCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StepCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae108db7_8765_4329_9908_059277dee586',
    
    class_name='StepCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ae108db7_8765_4329_9908_059277dee586',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StepCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    