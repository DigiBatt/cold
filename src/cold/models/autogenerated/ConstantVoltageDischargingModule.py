
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DischargingModule import Discharging



from .VoltageHoldModule import VoltageHold





from .MeasurementParameterModule import MeasurementParameter





class ConstantVoltageDischarging(Discharging, VoltageHold):
    """
    Class representing the `ConstantVoltageDischarging` entity, which inherits from:
    - Discharging, VoltageHold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9865e4f9_756d_4d94_a6fd_4102ab795f9e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantVoltageDischarging'`
        - **Alias**: `class_name`
    
    - `hasMeasurementParameter` (`Optional[MeasurementParameter]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementParameter`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantVoltageDischarging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9865e4f9_756d_4d94_a6fd_4102ab795f9e',
    
    class_name='ConstantVoltageDischarging',
    
    hasMeasurementParameter="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9865e4f9_756d_4d94_a6fd_4102ab795f9e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantVoltageDischarging',
        alias="class_name"
    )
    
    hasMeasurementParameter: Optional[MeasurementParameter] = Field(
        None,
        alias="hasMeasurementParameter"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasMeasurementParameter", pre=True, always=True)
    def validate_hasMeasurementParameter(cls, value):
        if value is not None and not isinstance(value, MeasurementParameter):
            raise ValueError(f"Field 'hasMeasurementParameter' must be an instance of 'MeasurementParameter' or its subclass.")
        return value
    
    

    

    