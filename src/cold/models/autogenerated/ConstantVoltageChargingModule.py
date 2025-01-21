
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltageHoldModule import VoltageHold





from .MeasurementParameterModule import MeasurementParameter





class ConstantVoltageCharging(VoltageHold):
    """
    Class representing the `ConstantVoltageCharging` entity, which inherits from:
    - VoltageHold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_acdeaa89_0e99_4941_8821_d5dea3d34912'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantVoltageCharging'`
        - **Alias**: `class_name`
    
    - `hasMeasurementParameter` (`Optional[MeasurementParameter]`): 
        - **Default Value**: `None`
        - **Alias**: `hasMeasurementParameter`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantVoltageCharging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_acdeaa89_0e99_4941_8821_d5dea3d34912',
    
    class_name='ConstantVoltageCharging',
    
    hasMeasurementParameter="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_acdeaa89_0e99_4941_8821_d5dea3d34912',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantVoltageCharging',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    @validator("hasMeasurementParameter", pre=True, always=True)
    def validate_hasMeasurementParameter(cls, value):
        if value is not None and not isinstance(value, MeasurementParameter):
            raise ValueError(f"Field 'hasMeasurementParameter' must be an instance of 'MeasurementParameter' or its subclass.")
        return value
    
    

    

    