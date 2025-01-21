
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemperatureLimitModule import TemperatureLimit







class MiniumumTemperature(TemperatureLimit):
    """
    Class representing the `MiniumumTemperature` entity, which inherits from:
    - TemperatureLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4747c51d_86ab_4684_a4fb_b05f5c405ea3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MiniumumTemperature'`
        - **Alias**: `class_name`
    
    - `newareLabel` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `newareLabel`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MiniumumTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4747c51d_86ab_4684_a4fb_b05f5c405ea3',
    
    class_name='MiniumumTemperature',
    
    newareLabel="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4747c51d_86ab_4684_a4fb_b05f5c405ea3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MiniumumTemperature',
        alias="class_name"
    )
    
    newareLabel: Optional[str] = Field(
        None,
        alias="newareLabel"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    