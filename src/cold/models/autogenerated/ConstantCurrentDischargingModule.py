
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DischargingModule import Discharging



from .CurrentHoldModule import CurrentHold





from .MeasurementParameterModule import MeasurementParameter





class ConstantCurrentDischarging(Discharging, CurrentHold):
    """
    Class representing the `ConstantCurrentDischarging` entity, which inherits from:
    - Discharging, CurrentHold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_53fe3f58_0802_41cf_af69_4784fc42cc30'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantCurrentDischarging'`
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
    obj = ConstantCurrentDischarging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_53fe3f58_0802_41cf_af69_4784fc42cc30',
    
    class_name='ConstantCurrentDischarging',
    
    hasMeasurementParameter="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_53fe3f58_0802_41cf_af69_4784fc42cc30',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantCurrentDischarging',
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
    
    

    

    