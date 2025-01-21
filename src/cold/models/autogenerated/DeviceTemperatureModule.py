
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CelsiusTemperatureModule import CelsiusTemperature







class DeviceTemperature(CelsiusTemperature):
    """
    Class representing the `DeviceTemperature` entity, which inherits from:
    - CelsiusTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_463950b9_fd8d_48de_a52d_b29cab026391'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DeviceTemperature'`
        - **Alias**: `class_name`
    
    - `batteryArchiveLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `batteryArchiveLabel`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DeviceTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_463950b9_fd8d_48de_a52d_b29cab026391',
    
    class_name='DeviceTemperature',
    
    batteryArchiveLabel="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_463950b9_fd8d_48de_a52d_b29cab026391',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DeviceTemperature',
        alias="class_name"
    )
    
    batteryArchiveLabel: Optional[str] = Field(
        None,
        alias="batteryArchiveLabel"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    