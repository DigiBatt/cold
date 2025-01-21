
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryCellModule import BatteryCell







class PotassiumBattery(BatteryCell):
    """
    Class representing the `PotassiumBattery` entity, which inherits from:
    - BatteryCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_a306c4d2_9f74_4910_8b42_52e33552cd90'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PotassiumBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PotassiumBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_a306c4d2_9f74_4910_8b42_52e33552cd90',
    
    class_name='PotassiumBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_a306c4d2_9f74_4910_8b42_52e33552cd90',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PotassiumBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    