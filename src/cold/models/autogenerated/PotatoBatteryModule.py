
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrimaryBatteryModule import PrimaryBattery







class PotatoBattery(PrimaryBattery):
    """
    Class representing the `PotatoBattery` entity, which inherits from:
    - PrimaryBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_b079217c_572e_4cc4_be38_a8388977085b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PotatoBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PotatoBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_b079217c_572e_4cc4_be38_a8388977085b',
    
    class_name='PotatoBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_b079217c_572e_4cc4_be38_a8388977085b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PotatoBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    