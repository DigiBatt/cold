
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RedoxFlowBatteryModule import RedoxFlowBattery







class MembranelessFlowBattery(RedoxFlowBattery):
    """
    Class representing the `MembranelessFlowBattery` entity, which inherits from:
    - RedoxFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_5ae0d63a_51a9_433f_b92b_da7fd66ace6e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MembranelessFlowBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MembranelessFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_5ae0d63a_51a9_433f_b92b_da7fd66ace6e',
    
    class_name='MembranelessFlowBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_5ae0d63a_51a9_433f_b92b_da7fd66ace6e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MembranelessFlowBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    