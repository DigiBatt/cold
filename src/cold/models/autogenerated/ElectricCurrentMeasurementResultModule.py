
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementResultModule import MeasurementResult







class ElectricCurrentMeasurementResult(MeasurementResult):
    """
    Class representing the `ElectricCurrentMeasurementResult` entity, which inherits from:
    - MeasurementResult

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7beef5fb_a406_4284_b85a_87d55cf46a0e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentMeasurementResult'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentMeasurementResult(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7beef5fb_a406_4284_b85a_87d55cf46a0e',
    
    class_name='ElectricCurrentMeasurementResult',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7beef5fb_a406_4284_b85a_87d55cf46a0e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentMeasurementResult',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    