
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class SquareWaveVoltammetryWaveform(ElectricPotentialSignal):
    """
    Class representing the `SquareWaveVoltammetryWaveform` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_210f3520_1ea3_4c86_aa89_4cd9a3bc5a5a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareWaveVoltammetryWaveform'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareWaveVoltammetryWaveform(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_210f3520_1ea3_4c86_aa89_4cd9a3bc5a5a',
    
    class_name='SquareWaveVoltammetryWaveform',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_210f3520_1ea3_4c86_aa89_4cd9a3bc5a5a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SquareWaveVoltammetryWaveform',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    