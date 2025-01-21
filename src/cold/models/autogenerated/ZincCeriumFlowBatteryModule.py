
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZincFlowBatteryModule import ZincFlowBattery







class ZincCeriumFlowBattery(ZincFlowBattery):
    """
    Class representing the `ZincCeriumFlowBattery` entity, which inherits from:
    - ZincFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_dfbafabe_e807_4343_9493_abef18b2232b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincCeriumFlowBattery'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincCeriumFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_dfbafabe_e807_4343_9493_abef18b2232b',
    
    class_name='ZincCeriumFlowBattery',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_dfbafabe_e807_4343_9493_abef18b2232b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincCeriumFlowBattery',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    