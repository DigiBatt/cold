
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FullFlowBatteryModule import FullFlowBattery







class AqueousOrganicFlowBattery(FullFlowBattery):
    """
    Class representing the `AqueousOrganicFlowBattery` entity, which inherits from:
    - FullFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_4a620a13_ef9f_40c7_8833_c6e0720ce3ca'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AqueousOrganicFlowBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AqueousOrganicFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_4a620a13_ef9f_40c7_8833_c6e0720ce3ca',
    
    class_name='AqueousOrganicFlowBattery',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_4a620a13_ef9f_40c7_8833_c6e0720ce3ca',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AqueousOrganicFlowBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    