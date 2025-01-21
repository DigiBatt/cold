
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class SquareWavePotentialWaveform(ElectricPotentialSignal):
    """
    Class representing the `SquareWavePotentialWaveform` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0e33278b_639f_412d_9abd_64c3790026ef'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareWavePotentialWaveform'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareWavePotentialWaveform(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0e33278b_639f_412d_9abd_64c3790026ef',
    
    class_name='SquareWavePotentialWaveform',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0e33278b_639f_412d_9abd_64c3790026ef',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SquareWavePotentialWaveform',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    