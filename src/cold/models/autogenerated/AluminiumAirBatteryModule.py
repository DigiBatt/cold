
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AluminiumBatteryModule import AluminiumBattery



from .MetalAirBatteryModule import MetalAirBattery





from .PositiveElectrodeModule import PositiveElectrode



from .NegativeElectrodeModule import NegativeElectrode





class AluminiumAirBattery(AluminiumBattery, MetalAirBattery):
    """
    Class representing the `AluminiumAirBattery` entity, which inherits from:
    - AluminiumBattery, MetalAirBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_44cb1e3b_480c_4594_a79a_4e4f001050ea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AluminiumAirBattery'`
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
    obj = AluminiumAirBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_44cb1e3b_480c_4594_a79a_4e4f001050ea',
    
    class_name='AluminiumAirBattery',
    
    hasPositiveElectrode="example_value",
    
    hasNegativeElectrode="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_44cb1e3b_480c_4594_a79a_4e4f001050ea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AluminiumAirBattery',
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
    
    

    

    