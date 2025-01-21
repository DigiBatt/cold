
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AqueousMetallicFlowBatteryModule import AqueousMetallicFlowBattery







class PolysulfideBromideFlowBattery(AqueousMetallicFlowBattery):
    """
    Class representing the `PolysulfideBromideFlowBattery` entity, which inherits from:
    - AqueousMetallicFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_a7034a6b_8d1c_4a28_9b8a_5bee39eedf59'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PolysulfideBromideFlowBattery'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PolysulfideBromideFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_a7034a6b_8d1c_4a28_9b8a_5bee39eedf59',
    
    class_name='PolysulfideBromideFlowBattery',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_a7034a6b_8d1c_4a28_9b8a_5bee39eedf59',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PolysulfideBromideFlowBattery',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    