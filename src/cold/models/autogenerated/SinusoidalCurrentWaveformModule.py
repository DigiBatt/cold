
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlternatingCurrentModule import AlternatingCurrent







class SinusoidalCurrentWaveform(AlternatingCurrent):
    """
    Class representing the `SinusoidalCurrentWaveform` entity, which inherits from:
    - AlternatingCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d61deb36_b397_4811_bf7a_66d8e4578c6e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SinusoidalCurrentWaveform'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SinusoidalCurrentWaveform(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d61deb36_b397_4811_bf7a_66d8e4578c6e',
    
    class_name='SinusoidalCurrentWaveform',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d61deb36_b397_4811_bf7a_66d8e4578c6e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SinusoidalCurrentWaveform',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    