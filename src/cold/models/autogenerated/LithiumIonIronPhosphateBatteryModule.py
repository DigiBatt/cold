
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LithiumIonBatteryModule import LithiumIonBattery





from .PositiveElectrodeModule import PositiveElectrode





class LithiumIonIronPhosphateBattery(LithiumIonBattery):
    """
    Class representing the `LithiumIonIronPhosphateBattery` entity, which inherits from:
    - LithiumIonBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_04a4e5a4_e6fd_43af_b1ca_4a16d5f8886c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumIonIronPhosphateBattery'`
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
    obj = LithiumIonIronPhosphateBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_04a4e5a4_e6fd_43af_b1ca_4a16d5f8886c',
    
    class_name='LithiumIonIronPhosphateBattery',
    
    wikidataReference="example_value",
    
    hasPositiveElectrode="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_04a4e5a4_e6fd_43af_b1ca_4a16d5f8886c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumIonIronPhosphateBattery',
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
    
    

    

    