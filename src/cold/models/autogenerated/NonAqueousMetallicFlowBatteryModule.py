
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FullFlowBatteryModule import FullFlowBattery







class NonAqueousMetallicFlowBattery(FullFlowBattery):
    """
    Class representing the `NonAqueousMetallicFlowBattery` entity, which inherits from:
    - FullFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_1191d114_5aec_4167_97b1_c0bca9414c49'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NonAqueousMetallicFlowBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NonAqueousMetallicFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_1191d114_5aec_4167_97b1_c0bca9414c49',
    
    class_name='NonAqueousMetallicFlowBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_1191d114_5aec_4167_97b1_c0bca9414c49',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NonAqueousMetallicFlowBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    