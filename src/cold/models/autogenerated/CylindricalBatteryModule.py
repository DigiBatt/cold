
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BatteryCellModule import BatteryCell





from .CaseModule import Case





class CylindricalBattery(BatteryCell):
    """
    Class representing the `CylindricalBattery` entity, which inherits from:
    - BatteryCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_ac604ecd_cc60_4b98_b57c_74cd5d3ccd40'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CylindricalBattery'`
        - **Alias**: `class_name`
    
    - `hasCase` (`Optional[Case]`): 
        - **Default Value**: `None`
        - **Alias**: `hasCase`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CylindricalBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_ac604ecd_cc60_4b98_b57c_74cd5d3ccd40',
    
    class_name='CylindricalBattery',
    
    hasCase="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_ac604ecd_cc60_4b98_b57c_74cd5d3ccd40',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CylindricalBattery',
        alias="class_name"
    )
    
    hasCase: Optional[Case] = Field(
        None,
        alias="hasCase"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    @validator("hasCase", pre=True, always=True)
    def validate_hasCase(cls, value):
        if value is not None and not isinstance(value, Case):
            raise ValueError(f"Field 'hasCase' must be an instance of 'Case' or its subclass.")
        return value
    
    

    

    