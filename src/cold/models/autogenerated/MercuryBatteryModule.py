
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZincBatteryModule import ZincBattery







class MercuryBattery(ZincBattery):
    """
    Class representing the `MercuryBattery` entity, which inherits from:
    - ZincBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_04d0ea52_8528_4e09_8751_2f55897a8f6e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MercuryBattery'`
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
    obj = MercuryBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_04d0ea52_8528_4e09_8751_2f55897a8f6e',
    
    class_name='MercuryBattery',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_04d0ea52_8528_4e09_8751_2f55897a8f6e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MercuryBattery',
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
    

    
    

    

    