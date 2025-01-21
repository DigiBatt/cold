
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity



from .ElectrochemicalPerformanceQuantityModule import ElectrochemicalPerformanceQuantity





from .MeasurementUnitModule import MeasurementUnit





class SpecificCapacity(ISQDerivedQuantity, ElectrochemicalPerformanceQuantity):
    """
    Class representing the `SpecificCapacity` entity, which inherits from:
    - ISQDerivedQuantity, ElectrochemicalPerformanceQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e3dc60d_dd6b_47d6_8161_70004fc5ee30'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpecificCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    - `newareLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `newareLabel`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpecificCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e3dc60d_dd6b_47d6_8161_70004fc5ee30',
    
    class_name='SpecificCapacity',
    
    elucidation="example_value",
    
    hasMeasurementUnit="example_value",
    
    newareLabel="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e3dc60d_dd6b_47d6_8161_70004fc5ee30',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpecificCapacity',
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
    
    newareLabel: Optional[str] = Field(
        None,
        alias="newareLabel"
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
    
    

    

    