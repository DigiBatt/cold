
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineCellModule import AlkalineCell



from .ZincAirBatteryModule import ZincAirBattery





from .ElectrolyteModule import Electrolyte



from .PositiveElectrodeModule import PositiveElectrode



from .NegativeElectrodeModule import NegativeElectrode





class AlkalineZincAirBattery(AlkalineCell, ZincAirBattery):
    """
    Class representing the `AlkalineZincAirBattery` entity, which inherits from:
    - AlkalineCell, ZincAirBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_b5910d2f_3114_4663_8d46_e418ff859251'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkalineZincAirBattery'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlkalineZincAirBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_b5910d2f_3114_4663_8d46_e418ff859251',
    
    class_name='AlkalineZincAirBattery',
    
    hasElectrolyte="example_value",
    
    hasPositiveElectrode="example_value",
    
    hasNegativeElectrode="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_b5910d2f_3114_4663_8d46_e418ff859251',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkalineZincAirBattery',
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
    
    

    

    