
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricPotentialSignalModule import ElectricPotentialSignal







class TriangularPotentialWaveform(ElectricPotentialSignal):
    """
    Class representing the `TriangularPotentialWaveform` entity, which inherits from:
    - ElectricPotentialSignal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f9af8440_3629_4558_a944_9dfaf3dfd7ec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TriangularPotentialWaveform'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TriangularPotentialWaveform(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f9af8440_3629_4558_a944_9dfaf3dfd7ec',
    
    class_name='TriangularPotentialWaveform',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f9af8440_3629_4558_a944_9dfaf3dfd7ec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TriangularPotentialWaveform',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    