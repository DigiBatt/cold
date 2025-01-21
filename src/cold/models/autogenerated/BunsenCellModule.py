
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WetCellModule import WetCell



from .ZincCarbonBatteryModule import ZincCarbonBattery







class BunsenCell(WetCell, ZincCarbonBattery):
    """
    Class representing the `BunsenCell` entity, which inherits from:
    - WetCell, ZincCarbonBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_70dad2a6_5316_4211_99a6_2031119515c1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BunsenCell'`
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
    obj = BunsenCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_70dad2a6_5316_4211_99a6_2031119515c1',
    
    class_name='BunsenCell',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_70dad2a6_5316_4211_99a6_2031119515c1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BunsenCell',
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
    

    
    

    

    