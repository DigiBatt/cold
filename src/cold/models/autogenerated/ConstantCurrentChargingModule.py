
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentHoldModule import CurrentHold



from .ChargingModule import Charging





from .MeasurementParameterModule import MeasurementParameter





class ConstantCurrentCharging(CurrentHold, Charging):
    """
    Class representing the `ConstantCurrentCharging` entity, which inherits from:
    - CurrentHold, Charging

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83f2b1e9_cb67_4dbf_977f_ba54bbae374f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantCurrentCharging'`
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
    obj = ConstantCurrentCharging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83f2b1e9_cb67_4dbf_977f_ba54bbae374f',
    
    class_name='ConstantCurrentCharging',
    
    hasMeasurementParameter="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_83f2b1e9_cb67_4dbf_977f_ba54bbae374f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantCurrentCharging',
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
    
    

    

    