
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementModule import Measurement







class TimeMeasurement(Measurement):
    """
    Class representing the `TimeMeasurement` entity, which inherits from:
    - Measurement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fdf65c1_b86a_4cbe_8c06_56321b425d4e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TimeMeasurement'`
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
    obj = TimeMeasurement(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fdf65c1_b86a_4cbe_8c06_56321b425d4e',
    
    class_name='TimeMeasurement',
    
    hasOutput="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7fdf65c1_b86a_4cbe_8c06_56321b425d4e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TimeMeasurement',
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
    

    
    

    

    