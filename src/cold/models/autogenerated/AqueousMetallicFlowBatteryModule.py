
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FullFlowBatteryModule import FullFlowBattery







class AqueousMetallicFlowBattery(FullFlowBattery):
    """
    Class representing the `AqueousMetallicFlowBattery` entity, which inherits from:
    - FullFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_edc98332_248a_436a_a352_5a7897150c4f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AqueousMetallicFlowBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AqueousMetallicFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_edc98332_248a_436a_a352_5a7897150c4f',
    
    class_name='AqueousMetallicFlowBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_edc98332_248a_436a_a352_5a7897150c4f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AqueousMetallicFlowBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    