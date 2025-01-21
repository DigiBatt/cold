
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WetCellModule import WetCell



from .ZincBatteryModule import ZincBattery







class GroveCell(WetCell, ZincBattery):
    """
    Class representing the `GroveCell` entity, which inherits from:
    - WetCell, ZincBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_bd44dba6_459e_4b66_8342_804b09a3a6b5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GroveCell'`
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
    obj = GroveCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_bd44dba6_459e_4b66_8342_804b09a3a6b5',
    
    class_name='GroveCell',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_bd44dba6_459e_4b66_8342_804b09a3a6b5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GroveCell',
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
    

    
    

    

    