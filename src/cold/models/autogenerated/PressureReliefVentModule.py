
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComponentModule import Component







class PressureReliefVent(Component):
    """
    Class representing the `PressureReliefVent` entity, which inherits from:
    - Component

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f330680b_347e_45b3_9113_5ce09d18d60b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PressureReliefVent'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PressureReliefVent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f330680b_347e_45b3_9113_5ce09d18d60b',
    
    class_name='PressureReliefVent',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f330680b_347e_45b3_9113_5ce09d18d60b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PressureReliefVent',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    