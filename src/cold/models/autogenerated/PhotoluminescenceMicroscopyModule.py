
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MicroscopyModule import Microscopy







class PhotoluminescenceMicroscopy(Microscopy):
    """
    Class representing the `PhotoluminescenceMicroscopy` entity, which inherits from:
    - Microscopy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PhotoluminescenceMicroscopy'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhotoluminescenceMicroscopy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhotoluminescenceMicroscopy(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#PhotoluminescenceMicroscopy',
    
    class_name='PhotoluminescenceMicroscopy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PhotoluminescenceMicroscopy',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhotoluminescenceMicroscopy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    