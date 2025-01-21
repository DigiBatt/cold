
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MesonModule import Meson







class PseudoscalarMeson(Meson):
    """
    Class representing the `PseudoscalarMeson` entity, which inherits from:
    - Meson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_12aae025_a226_4762_9d51_81200a8ce54c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PseudoscalarMeson'`
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
    obj = PseudoscalarMeson(
    
    class_iri='https://w3id.org/emmo#EMMO_12aae025_a226_4762_9d51_81200a8ce54c',
    
    class_name='PseudoscalarMeson',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_12aae025_a226_4762_9d51_81200a8ce54c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PseudoscalarMeson',
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
    

    
    

    

    