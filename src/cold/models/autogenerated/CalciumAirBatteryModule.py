
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumBatteryModule import CalciumBattery



from .MetalAirBatteryModule import MetalAirBattery







class CalciumAirBattery(CalciumBattery, MetalAirBattery):
    """
    Class representing the `CalciumAirBattery` entity, which inherits from:
    - CalciumBattery, MetalAirBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_eeab063b_9dbf_4879_8008_44e5c4a34f1f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumAirBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumAirBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_eeab063b_9dbf_4879_8008_44e5c4a34f1f',
    
    class_name='CalciumAirBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_eeab063b_9dbf_4879_8008_44e5c4a34f1f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumAirBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    