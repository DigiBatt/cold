
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryCellModule import BatteryCell







class SiliconBattery(BatteryCell):
    """
    Class representing the `SiliconBattery` entity, which inherits from:
    - BatteryCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_9d1bf61e_7f64_43fd_af38_c16fb04ee72d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SiliconBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SiliconBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_9d1bf61e_7f64_43fd_af38_c16fb04ee72d',
    
    class_name='SiliconBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_9d1bf61e_7f64_43fd_af38_c16fb04ee72d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SiliconBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    