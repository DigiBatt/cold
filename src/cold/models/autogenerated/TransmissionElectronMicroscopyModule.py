
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MicroscopyModule import Microscopy







class TransmissionElectronMicroscopy(Microscopy):
    """
    Class representing the `TransmissionElectronMicroscopy` entity, which inherits from:
    - Microscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#TransmissionElectronMicroscopy'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransmissionElectronMicroscopy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TransmissionElectronMicroscopy(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#TransmissionElectronMicroscopy',
    
    class_name='TransmissionElectronMicroscopy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#TransmissionElectronMicroscopy',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransmissionElectronMicroscopy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    