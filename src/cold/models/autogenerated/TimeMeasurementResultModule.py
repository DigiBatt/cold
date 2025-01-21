
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementResultModule import MeasurementResult







class TimeMeasurementResult(MeasurementResult):
    """
    Class representing the `TimeMeasurementResult` entity, which inherits from:
    - MeasurementResult

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_496c8f31_9732_42c1_8eae_dd73979c06eb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TimeMeasurementResult'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TimeMeasurementResult(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_496c8f31_9732_42c1_8eae_dd73979c06eb',
    
    class_name='TimeMeasurementResult',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_496c8f31_9732_42c1_8eae_dd73979c06eb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TimeMeasurementResult',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    