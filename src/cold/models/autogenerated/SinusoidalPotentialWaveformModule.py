
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class SinusoidalPotentialWaveform(ElectricPotentialSignal):
    """
    Class representing the `SinusoidalPotentialWaveform` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c74bb11c_e875_4112_b9cf_00d0890ef1f5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SinusoidalPotentialWaveform'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SinusoidalPotentialWaveform(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c74bb11c_e875_4112_b9cf_00d0890ef1f5',
    
    class_name='SinusoidalPotentialWaveform',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c74bb11c_e875_4112_b9cf_00d0890ef1f5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SinusoidalPotentialWaveform',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    