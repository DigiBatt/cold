
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineCellModule import AlkalineCell



from .ZincCarbonBatteryModule import ZincCarbonBattery





from .ElectrolyteModule import Electrolyte



from .PositiveElectrodeModule import PositiveElectrode



from .NegativeElectrodeModule import NegativeElectrode





class AlkalineZincManganeseDioxideBattery(AlkalineCell, ZincCarbonBattery):
    """
    Class representing the `AlkalineZincManganeseDioxideBattery` entity, which inherits from:
    - AlkalineCell, ZincCarbonBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_b572826a_b4e4_4986_b57d_f7b945061f8b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkalineZincManganeseDioxideBattery'`
        - **Alias**: `class_name`
    
    - `hasElectrolyte` (`Optional[Electrolyte]`): 
        - **Default Value**: `None`
        - **Alias**: `hasElectrolyte`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
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
    obj = AlkalineZincManganeseDioxideBattery(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_b572826a_b4e4_4986_b57d_f7b945061f8b',
    
    class_name='AlkalineZincManganeseDioxideBattery',
    
    hasElectrolyte="example_value",
    
    wikidataReference="example_value",
    
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
        'https://w3id.org/emmo/domain/battery#battery_b572826a_b4e4_4986_b57d_f7b945061f8b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkalineZincManganeseDioxideBattery',
        alias="class_name"
    )
    
    hasElectrolyte: Optional[Electrolyte] = Field(
        None,
        alias="hasElectrolyte"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
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
    
    

    

    