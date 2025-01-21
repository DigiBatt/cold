
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MicroscopyModule import Microscopy







class AtomicForceMicroscopy(Microscopy):
    """
    Class representing the `AtomicForceMicroscopy` entity, which inherits from:
    - Microscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#AtomicForceMicroscopy'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AtomicForceMicroscopy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AtomicForceMicroscopy(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#AtomicForceMicroscopy',
    
    class_name='AtomicForceMicroscopy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#AtomicForceMicroscopy',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AtomicForceMicroscopy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    