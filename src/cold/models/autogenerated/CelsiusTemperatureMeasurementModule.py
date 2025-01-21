
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementModule import Measurement







class CelsiusTemperatureMeasurement(Measurement):
    """
    Class representing the `CelsiusTemperatureMeasurement` entity, which inherits from:
    - Measurement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bea04148_10d9_4eda_9cd5_8f609d7e9ff8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CelsiusTemperatureMeasurement'`
        - **Alias**: `class_name`
    
    - `hasOutput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasOutput`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CelsiusTemperatureMeasurement(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bea04148_10d9_4eda_9cd5_8f609d7e9ff8',
    
    class_name='CelsiusTemperatureMeasurement',
    
    hasOutput="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bea04148_10d9_4eda_9cd5_8f609d7e9ff8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CelsiusTemperatureMeasurement',
        alias="class_name"
    )
    
    hasOutput: Optional[str] = Field(
        None,
        alias="hasOutput"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    