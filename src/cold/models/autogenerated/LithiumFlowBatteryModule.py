
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HybridFlowBatteryModule import HybridFlowBattery



from .LithiumBatteryModule import LithiumBattery







class LithiumFlowBattery(HybridFlowBattery, LithiumBattery):
    """
    Class representing the `LithiumFlowBattery` entity, which inherits from:
    - HybridFlowBattery, LithiumBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_74f06cdd_1f07_4e4f_9aac_21ffc4eba5ad'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumFlowBattery'`
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
    obj = LithiumFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_74f06cdd_1f07_4e4f_9aac_21ffc4eba5ad',
    
    class_name='LithiumFlowBattery',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_74f06cdd_1f07_4e4f_9aac_21ffc4eba5ad',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumFlowBattery',
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
    

    
    

    

    