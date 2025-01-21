
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetalAirBatteryModule import MetalAirBattery



from .SiliconBatteryModule import SiliconBattery





from .PositiveElectrodeModule import PositiveElectrode



from .NegativeElectrodeModule import NegativeElectrode





class SiliconAirBattery(MetalAirBattery, SiliconBattery):
    """
    Class representing the `SiliconAirBattery` entity, which inherits from:
    - MetalAirBattery, SiliconBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_67c336e7_4d06_44b0_8f4d_5ab0c4d12a92'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SiliconAirBattery'`
        - **Alias**: `class_name`
    
    - `hasPositiveElectrode` (`Optional[PositiveElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPositiveElectrode`
    
    - `hasNegativeElectrode` (`Optional[NegativeElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNegativeElectrode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SiliconAirBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_67c336e7_4d06_44b0_8f4d_5ab0c4d12a92',
    
    class_name='SiliconAirBattery',
    
    hasPositiveElectrode="example_value",
    
    hasNegativeElectrode="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_67c336e7_4d06_44b0_8f4d_5ab0c4d12a92',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SiliconAirBattery',
        alias="class_name"
    )
    
    hasPositiveElectrode: Optional[PositiveElectrode] = Field(
        None,
        alias="hasPositiveElectrode"
    )
    
    hasNegativeElectrode: Optional[NegativeElectrode] = Field(
        None,
        alias="hasNegativeElectrode"
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
    
    @validator("hasNegativeElectrode", pre=True, always=True)
    def validate_hasNegativeElectrode(cls, value):
        if value is not None and not isinstance(value, NegativeElectrode):
            raise ValueError(f"Field 'hasNegativeElectrode' must be an instance of 'NegativeElectrode' or its subclass.")
        return value
    
    

    

    