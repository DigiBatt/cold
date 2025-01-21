
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConstantCurrentChargingModule import ConstantCurrentCharging



from .CurrentPulsingModule import CurrentPulsing





from .MeasurementParameterModule import MeasurementParameter





class PulseCharging(ConstantCurrentCharging, CurrentPulsing):
    """
    Class representing the `PulseCharging` entity, which inherits from:
    - ConstantCurrentCharging, CurrentPulsing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8372fdaa_dc01_4abf_9b75_442d0b28f263'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PulseCharging'`
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
    obj = PulseCharging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8372fdaa_dc01_4abf_9b75_442d0b28f263',
    
    class_name='PulseCharging',
    
    hasMeasurementParameter="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_8372fdaa_dc01_4abf_9b75_442d0b28f263',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PulseCharging',
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
    
    

    

    