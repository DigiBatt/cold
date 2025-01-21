
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrimaryBatteryModule import PrimaryBattery







class FrogBattery(PrimaryBattery):
    """
    Class representing the `FrogBattery` entity, which inherits from:
    - PrimaryBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_a48145f2_ba93_40c1_a4f7_0017ccff02b4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FrogBattery'`
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
    obj = FrogBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_a48145f2_ba93_40c1_a4f7_0017ccff02b4',
    
    class_name='FrogBattery',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_a48145f2_ba93_40c1_a4f7_0017ccff02b4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FrogBattery',
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
    

    
    

    

    