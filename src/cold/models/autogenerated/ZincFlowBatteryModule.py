
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HybridFlowBatteryModule import HybridFlowBattery



from .ZincBatteryModule import ZincBattery







class ZincFlowBattery(HybridFlowBattery, ZincBattery):
    """
    Class representing the `ZincFlowBattery` entity, which inherits from:
    - HybridFlowBattery, ZincBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_5afce525_90b7_4807_87f0_ab23a52a0320'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincFlowBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_5afce525_90b7_4807_87f0_ab23a52a0320',
    
    class_name='ZincFlowBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_5afce525_90b7_4807_87f0_ab23a52a0320',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincFlowBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    