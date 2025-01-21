
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntensiveModule import Intensive



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity





from .MeasurementUnitModule import MeasurementUnit





class EnergyDensity(Intensive, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `EnergyDensity` entity, which inherits from:
    - Intensive, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4aa1b96e_44a0_4b1a_a0ac_723d0223d80b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EnergyDensity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EnergyDensity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4aa1b96e_44a0_4b1a_a0ac_723d0223d80b',
    
    class_name='EnergyDensity',
    
    elucidation="example_value",
    
    hasMeasurementUnit="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4aa1b96e_44a0_4b1a_a0ac_723d0223d80b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EnergyDensity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasMeasurementUnit: Optional[MeasurementUnit] = Field(
        None,
        alias="hasMeasurementUnit"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    @validator("hasMeasurementUnit", pre=True, always=True)
    def validate_hasMeasurementUnit(cls, value):
        if value is not None and not isinstance(value, MeasurementUnit):
            raise ValueError(f"Field 'hasMeasurementUnit' must be an instance of 'MeasurementUnit' or its subclass.")
        return value
    
    

    

    