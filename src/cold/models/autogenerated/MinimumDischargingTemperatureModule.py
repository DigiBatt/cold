
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MiniumumTemperatureModule import MiniumumTemperature







class MinimumDischargingTemperature(MiniumumTemperature):
    """
    Class representing the `MinimumDischargingTemperature` entity, which inherits from:
    - MiniumumTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2a1de79f_e927_45a2_9619_3799a0d61e9b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MinimumDischargingTemperature'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MinimumDischargingTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2a1de79f_e927_45a2_9619_3799a0d61e9b',
    
    class_name='MinimumDischargingTemperature',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2a1de79f_e927_45a2_9619_3799a0d61e9b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MinimumDischargingTemperature',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    