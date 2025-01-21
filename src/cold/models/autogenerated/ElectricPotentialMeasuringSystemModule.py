
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasuringSystemModule import MeasuringSystem







class ElectricPotentialMeasuringSystem(MeasuringSystem):
    """
    Class representing the `ElectricPotentialMeasuringSystem` entity, which inherits from:
    - MeasuringSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3f9b2956_1465_4fe0_b0df_5e4784dac3b6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricPotentialMeasuringSystem'`
        - **Alias**: `class_name`
    
    - `hasPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricPotentialMeasuringSystem(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3f9b2956_1465_4fe0_b0df_5e4784dac3b6',
    
    class_name='ElectricPotentialMeasuringSystem',
    
    hasPart="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3f9b2956_1465_4fe0_b0df_5e4784dac3b6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricPotentialMeasuringSystem',
        alias="class_name"
    )
    
    hasPart: Optional[str] = Field(
        None,
        alias="hasPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    