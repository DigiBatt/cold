
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZincCarbonBatteryModule import ZincCarbonBattery





from .ElectrolyteModule import Electrolyte



from .PositiveElectrodeModule import PositiveElectrode



from .NegativeElectrodeModule import NegativeElectrode





class ZincChlorideBattery(ZincCarbonBattery):
    """
    Class representing the `ZincChlorideBattery` entity, which inherits from:
    - ZincCarbonBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_55a8a42d_0f83_473d_82b0_32640114b7db'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincChlorideBattery'`
        - **Alias**: `class_name`
    
    - `hasElectrolyte` (`Optional[Electrolyte]`): 
        - **Default Value**: `None`
        - **Alias**: `hasElectrolyte`
    
    - `hasPositiveElectrode` (`Optional[PositiveElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPositiveElectrode`
    
    - `hasNegativeElectrode` (`Optional[NegativeElectrode]`): 
        - **Default Value**: `None`
        - **Alias**: `hasNegativeElectrode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincChlorideBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_55a8a42d_0f83_473d_82b0_32640114b7db',
    
    class_name='ZincChlorideBattery',
    
    hasElectrolyte="example_value",
    
    hasPositiveElectrode="example_value",
    
    hasNegativeElectrode="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_55a8a42d_0f83_473d_82b0_32640114b7db',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincChlorideBattery',
        alias="class_name"
    )
    
    hasElectrolyte: Optional[Electrolyte] = Field(
        None,
        alias="hasElectrolyte"
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasElectrolyte", pre=True, always=True)
    def validate_hasElectrolyte(cls, value):
        if value is not None and not isinstance(value, Electrolyte):
            raise ValueError(f"Field 'hasElectrolyte' must be an instance of 'Electrolyte' or its subclass.")
        return value
    
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
    
    

    

    