
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AqueousMetallicFlowBatteryModule import AqueousMetallicFlowBattery







class VanadiumRedoxFlowBattery(AqueousMetallicFlowBattery):
    """
    Class representing the `VanadiumRedoxFlowBattery` entity, which inherits from:
    - AqueousMetallicFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_e2aac68e_f880_4be5_87e6_73eba9f75955'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VanadiumRedoxFlowBattery'`
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
    obj = VanadiumRedoxFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_e2aac68e_f880_4be5_87e6_73eba9f75955',
    
    class_name='VanadiumRedoxFlowBattery',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_e2aac68e_f880_4be5_87e6_73eba9f75955',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VanadiumRedoxFlowBattery',
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
    

    
    

    

    