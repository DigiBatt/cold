
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZincFlowBatteryModule import ZincFlowBattery





from .PositiveElectrodeModule import PositiveElectrode





class ZincBromineFlowBattery(ZincFlowBattery):
    """
    Class representing the `ZincBromineFlowBattery` entity, which inherits from:
    - ZincFlowBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_7b28d3a1_24d5_477b_afd8_af2bac480724'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincBromineFlowBattery'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `hasPositiveElectrode` (`Optional[PositiveElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPositiveElectrode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincBromineFlowBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_7b28d3a1_24d5_477b_afd8_af2bac480724',
    
    class_name='ZincBromineFlowBattery',
    
    wikidataReference="example_value",
    
    hasPositiveElectrode="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_7b28d3a1_24d5_477b_afd8_af2bac480724',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincBromineFlowBattery',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    hasPositiveElectrode: Optional[PositiveElectrode] = Field(
        None,
        alias="hasPositiveElectrode"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasPositiveElectrode", pre=True, always=True)
    def validate_hasPositiveElectrode(cls, value):
        if value is not None and not isinstance(value, PositiveElectrode):
            raise ValueError(f"Field 'hasPositiveElectrode' must be an instance of 'PositiveElectrode' or its subclass.")
        return value
    
    

    

    