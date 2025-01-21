
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CelsiusTemperatureModule import CelsiusTemperature







class AmbientCelsiusTemperature(CelsiusTemperature):
    """
    Class representing the `AmbientCelsiusTemperature` entity, which inherits from:
    - CelsiusTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abd08921_6f3b_4a48_811e_7685c58aec0b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmbientCelsiusTemperature'`
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
    obj = AmbientCelsiusTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abd08921_6f3b_4a48_811e_7685c58aec0b',
    
    class_name='AmbientCelsiusTemperature',
    
    batteryArchiveLabel="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abd08921_6f3b_4a48_811e_7685c58aec0b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmbientCelsiusTemperature',
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
    

    
    

    

    