
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FullFlowBatteryModule import FullFlowBattery







class NonAqueousOrganicFlowBattery(FullFlowBattery):
    """
    Class representing the `NonAqueousOrganicFlowBattery` entity, which inherits from:
    - FullFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_5555b4bc_216e_4772_a914_b66b6e783079'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NonAqueousOrganicFlowBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NonAqueousOrganicFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_5555b4bc_216e_4772_a914_b66b6e783079',
    
    class_name='NonAqueousOrganicFlowBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_5555b4bc_216e_4772_a914_b66b6e783079',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NonAqueousOrganicFlowBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    