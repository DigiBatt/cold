
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZincFlowBatteryModule import ZincFlowBattery







class ZincChlorineFlowBattery(ZincFlowBattery):
    """
    Class representing the `ZincChlorineFlowBattery` entity, which inherits from:
    - ZincFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_820f837e_ec1c_40d7_a63a_cac3f9d91e6b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincChlorineFlowBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincChlorineFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_820f837e_ec1c_40d7_a63a_cac3f9d91e6b',
    
    class_name='ZincChlorineFlowBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_820f837e_ec1c_40d7_a63a_cac3f9d91e6b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincChlorineFlowBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    