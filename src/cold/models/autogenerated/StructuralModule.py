
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerspectiveModule import Perspective







class Structural(Perspective):
    """
    Class representing the `Structural` entity, which inherits from:
    - Perspective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_32e701c0_a925_49df_9829_0931b8554807'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Structural'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Structural(
    
    class_iri='https://w3id.org/emmo#EMMO_32e701c0_a925_49df_9829_0931b8554807',
    
    class_name='Structural',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_32e701c0_a925_49df_9829_0931b8554807',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Structural',
        alias="class_name"
    )
    

    
    

    

    