
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MiniumumTemperatureModule import MiniumumTemperature







class MinimumChargingTemperature(MiniumumTemperature):
    """
    Class representing the `MinimumChargingTemperature` entity, which inherits from:
    - MiniumumTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b90b1ad7_b9a8_44df_ad45_bfd25aac2e49'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MinimumChargingTemperature'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MinimumChargingTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b90b1ad7_b9a8_44df_ad45_bfd25aac2e49',
    
    class_name='MinimumChargingTemperature',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b90b1ad7_b9a8_44df_ad45_bfd25aac2e49',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MinimumChargingTemperature',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    