
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity





from .MeasurementUnitModule import MeasurementUnit





class SignalReferencePotential(ElectrochemicalControlQuantity):
    """
    Class representing the `SignalReferencePotential` entity, which inherits from:
    - ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_68059d94_4c21_4065_b329_07faeebc7e87'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SignalReferencePotential'`
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
    obj = SignalReferencePotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_68059d94_4c21_4065_b329_07faeebc7e87',
    
    class_name='SignalReferencePotential',
    
    elucidation="example_value",
    
    hasMeasurementUnit="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_68059d94_4c21_4065_b329_07faeebc7e87',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SignalReferencePotential',
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
    
    

    

    