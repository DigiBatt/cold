
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerspectiveModule import Perspective







class Semiotics(Perspective):
    """
    Class representing the `Semiotics` entity, which inherits from:
    - Perspective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8bb6b688_812a_4cb9_b76c_d5a058928719'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Semiotics'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Semiotics(
    
    class_iri='https://w3id.org/emmo#EMMO_8bb6b688_812a_4cb9_b76c_d5a058928719',
    
    class_name='Semiotics',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8bb6b688_812a_4cb9_b76c_d5a058928719',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Semiotics',
        alias="class_name"
    )
    

    
    

    

    