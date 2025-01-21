
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LithiumIonBatteryModule import LithiumIonBattery





from .NegativeElectrodeModule import NegativeElectrode





class LithiumIonGraphiteBattery(LithiumIonBattery):
    """
    Class representing the `LithiumIonGraphiteBattery` entity, which inherits from:
    - LithiumIonBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_2018e0da_4c25_46e9_83db_38431fc81ce0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumIonGraphiteBattery'`
        - **Alias**: `class_name`
    
    - `hasNegativeElectrode` (`Optional[NegativeElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNegativeElectrode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumIonGraphiteBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_2018e0da_4c25_46e9_83db_38431fc81ce0',
    
    class_name='LithiumIonGraphiteBattery',
    
    hasNegativeElectrode="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_2018e0da_4c25_46e9_83db_38431fc81ce0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumIonGraphiteBattery',
        alias="class_name"
    )
    
    hasNegativeElectrode: Optional[NegativeElectrode] = Field(
        None,
        alias="hasNegativeElectrode"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasNegativeElectrode", pre=True, always=True)
    def validate_hasNegativeElectrode(cls, value):
        if value is not None and not isinstance(value, NegativeElectrode):
            raise ValueError(f"Field 'hasNegativeElectrode' must be an instance of 'NegativeElectrode' or its subclass.")
        return value
    
    

    

    