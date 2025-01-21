
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumBatteryModule import CalciumBattery





from .PositiveElectrodeModule import PositiveElectrode





class CalciumSulfurBattery(CalciumBattery):
    """
    Class representing the `CalciumSulfurBattery` entity, which inherits from:
    - CalciumBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_e3717684_26bd_40ce_b279_e7b39cc3e67e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumSulfurBattery'`
        - **Alias**: `class_name`
    
    - `hasPositiveElectrode` (`Optional[PositiveElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPositiveElectrode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumSulfurBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_e3717684_26bd_40ce_b279_e7b39cc3e67e',
    
    class_name='CalciumSulfurBattery',
    
    hasPositiveElectrode="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_e3717684_26bd_40ce_b279_e7b39cc3e67e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumSulfurBattery',
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
    

    
    @validator("hasPositiveElectrode", pre=True, always=True)
    def validate_hasPositiveElectrode(cls, value):
        if value is not None and not isinstance(value, PositiveElectrode):
            raise ValueError(f"Field 'hasPositiveElectrode' must be an instance of 'PositiveElectrode' or its subclass.")
        return value
    
    

    

    