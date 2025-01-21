
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PulseCurrentModule import PulseCurrent



from .CurrentLimitModule import CurrentLimit







class MaximumPulseDischargingCurrent(PulseCurrent, CurrentLimit):
    """
    Class representing the `MaximumPulseDischargingCurrent` entity, which inherits from:
    - PulseCurrent, CurrentLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3e54f9e3_a31d_4821_9bfb_ef953a42c35b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumPulseDischargingCurrent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaximumPulseDischargingCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3e54f9e3_a31d_4821_9bfb_ef953a42c35b',
    
    class_name='MaximumPulseDischargingCurrent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3e54f9e3_a31d_4821_9bfb_ef953a42c35b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumPulseDischargingCurrent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    