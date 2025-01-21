
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryCellModule import BatteryCell







class DryChargedBattery(BatteryCell):
    """
    Class representing the `DryChargedBattery` entity, which inherits from:
    - BatteryCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_a1924455_6f7e_4a2d_afd3_95527523183a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DryChargedBattery'`
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
    obj = DryChargedBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_a1924455_6f7e_4a2d_afd3_95527523183a',
    
    class_name='DryChargedBattery',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_a1924455_6f7e_4a2d_afd3_95527523183a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DryChargedBattery',
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
    

    
    

    

    