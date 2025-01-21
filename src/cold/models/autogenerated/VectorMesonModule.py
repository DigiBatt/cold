
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MesonModule import Meson







class VectorMeson(Meson):
    """
    Class representing the `VectorMeson` entity, which inherits from:
    - Meson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1b32a555_978b_4e56_933f_e158e165023e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VectorMeson'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VectorMeson(
    
    class_iri='https://w3id.org/emmo#EMMO_1b32a555_978b_4e56_933f_e158e165023e',
    
    class_name='VectorMeson',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1b32a555_978b_4e56_933f_e158e165023e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VectorMeson',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    