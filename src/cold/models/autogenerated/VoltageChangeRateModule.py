
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalQuantityModule import ElectrochemicalQuantity





from .MeasurementUnitModule import MeasurementUnit





class VoltageChangeRate(ElectrochemicalQuantity):
    """
    Class representing the `VoltageChangeRate` entity, which inherits from:
    - ElectrochemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6f45881_9bf1_4cf5_988b_de79dab718ef'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VoltageChangeRate'`
        - **Alias**: `class_name`
    
    - `arbinLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `arbinLabel`
    
    - `novonixLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `novonixLabel`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasMeasurementUnit` (`Optional[MeasurementUnit]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementUnit`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VoltageChangeRate(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6f45881_9bf1_4cf5_988b_de79dab718ef',
    
    class_name='VoltageChangeRate',
    
    arbinLabel="example_value",
    
    novonixLabel="example_value",
    
    elucidation="example_value",
    
    hasMeasurementUnit="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6f45881_9bf1_4cf5_988b_de79dab718ef',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VoltageChangeRate',
        alias="class_name"
    )
    
    arbinLabel: Optional[str] = Field(
        None,
        alias="arbinLabel"
    )
    
    novonixLabel: Optional[str] = Field(
        None,
        alias="novonixLabel"
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
    
    

    

    