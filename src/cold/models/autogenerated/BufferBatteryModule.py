
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryModule import Battery



from .HolisticSystemModule import HolisticSystem







class BufferBattery(Battery, HolisticSystem):
    """
    Class representing the `BufferBattery` entity, which inherits from:
    - Battery, HolisticSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_dbc86554_1a2a_4f2b_b8c2_e793fa219883'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BufferBattery'`
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
    obj = BufferBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_dbc86554_1a2a_4f2b_b8c2_e793fa219883',
    
    class_name='BufferBattery',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_dbc86554_1a2a_4f2b_b8c2_e793fa219883',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BufferBattery',
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
    

    
    

    

    