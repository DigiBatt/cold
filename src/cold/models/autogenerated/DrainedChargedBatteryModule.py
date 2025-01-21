
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryCellModule import BatteryCell







class DrainedChargedBattery(BatteryCell):
    """
    Class representing the `DrainedChargedBattery` entity, which inherits from:
    - BatteryCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_4688d93e_1c2b_4ff0_8a12_b2e540d8a737'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DrainedChargedBattery'`
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
    obj = DrainedChargedBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_4688d93e_1c2b_4ff0_8a12_b2e540d8a737',
    
    class_name='DrainedChargedBattery',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_4688d93e_1c2b_4ff0_8a12_b2e540d8a737',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DrainedChargedBattery',
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
    

    
    

    

    