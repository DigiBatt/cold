
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OpenCircuitHoldModule import OpenCircuitHold



from .CurrentHoldModule import CurrentHold





from .MeasurementParameterModule import MeasurementParameter





class Resting(OpenCircuitHold, CurrentHold):
    """
    Class representing the `Resting` entity, which inherits from:
    - OpenCircuitHold, CurrentHold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_35469eeb_7fc3_4317_a4b5_b3be7015444b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Resting'`
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
    obj = Resting(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_35469eeb_7fc3_4317_a4b5_b3be7015444b',
    
    class_name='Resting',
    
    hasMeasurementParameter="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_35469eeb_7fc3_4317_a4b5_b3be7015444b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Resting',
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
    
    

    

    