
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZincBatteryModule import ZincBattery





from .PositiveElectrodeModule import PositiveElectrode





class ZincCarbonBattery(ZincBattery):
    """
    Class representing the `ZincCarbonBattery` entity, which inherits from:
    - ZincBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_aaaa6f4b_435b_425b_acb1_e8a427c3489a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincCarbonBattery'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `hasPositiveElectrode` (`Optional[PositiveElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPositiveElectrode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincCarbonBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_aaaa6f4b_435b_425b_acb1_e8a427c3489a',
    
    class_name='ZincCarbonBattery',
    
    IEVReference="example_value",
    
    hasPositiveElectrode="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_aaaa6f4b_435b_425b_acb1_e8a427c3489a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincCarbonBattery',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
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
    
    

    

    