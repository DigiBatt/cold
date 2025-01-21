
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LithiumIonBatteryModule import LithiumIonBattery





from .PositiveElectrodeModule import PositiveElectrode





class LithiumIonManganeseIronPhosphateBattery(LithiumIonBattery):
    """
    Class representing the `LithiumIonManganeseIronPhosphateBattery` entity, which inherits from:
    - LithiumIonBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_c429bb30_50d6_4cec_ae7e_279f59c36ccd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumIonManganeseIronPhosphateBattery'`
        - **Alias**: `class_name`
    
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
    obj = LithiumIonManganeseIronPhosphateBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_c429bb30_50d6_4cec_ae7e_279f59c36ccd',
    
    class_name='LithiumIonManganeseIronPhosphateBattery',
    
    hasPositiveElectrode="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_c429bb30_50d6_4cec_ae7e_279f59c36ccd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumIonManganeseIronPhosphateBattery',
        alias="class_name"
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
    
    

    

    