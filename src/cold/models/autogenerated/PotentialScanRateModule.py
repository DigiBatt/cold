
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ISQDerivedQuantityModule import ISQDerivedQuantity



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity





from .MeasurementUnitModule import MeasurementUnit





class PotentialScanRate(ISQDerivedQuantity, ElectrochemicalControlQuantity):
    """
    Class representing the `PotentialScanRate` entity, which inherits from:
    - ISQDerivedQuantity, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_264f40d1_17c9_4bc7_9c47_5cfb18132278'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PotentialScanRate'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PotentialScanRate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_264f40d1_17c9_4bc7_9c47_5cfb18132278',
    
    class_name='PotentialScanRate',
    
    elucidation="example_value",
    
    hasMeasurementUnit="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_264f40d1_17c9_4bc7_9c47_5cfb18132278',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PotentialScanRate',
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
    

    
    @validator("hasMeasurementUnit", pre=True, always=True)
    def validate_hasMeasurementUnit(cls, value):
        if value is not None and not isinstance(value, MeasurementUnit):
            raise ValueError(f"Field 'hasMeasurementUnit' must be an instance of 'MeasurementUnit' or its subclass.")
        return value
    
    

    

    