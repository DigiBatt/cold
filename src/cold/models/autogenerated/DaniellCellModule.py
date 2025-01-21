
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WetCellModule import WetCell



from .ZincBatteryModule import ZincBattery







class DaniellCell(WetCell, ZincBattery):
    """
    Class representing the `DaniellCell` entity, which inherits from:
    - WetCell, ZincBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_d94a5498_321a_43d3_af62_80f8253068a9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DaniellCell'`
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
    obj = DaniellCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_d94a5498_321a_43d3_af62_80f8253068a9',
    
    class_name='DaniellCell',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_d94a5498_321a_43d3_af62_80f8253068a9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DaniellCell',
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
    

    
    

    

    