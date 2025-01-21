
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AqueousMetallicFlowBatteryModule import AqueousMetallicFlowBattery







class IronRedoxFlowBattery(AqueousMetallicFlowBattery):
    """
    Class representing the `IronRedoxFlowBattery` entity, which inherits from:
    - AqueousMetallicFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_31a80cd5_d4eb_4f7d_a990_f32a5a75ea86'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IronRedoxFlowBattery'`
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
    obj = IronRedoxFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_31a80cd5_d4eb_4f7d_a990_f32a5a75ea86',
    
    class_name='IronRedoxFlowBattery',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_31a80cd5_d4eb_4f7d_a990_f32a5a75ea86',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IronRedoxFlowBattery',
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
    

    
    

    

    