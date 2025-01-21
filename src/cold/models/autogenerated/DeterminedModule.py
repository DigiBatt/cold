
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeclaredModule import Declared







class Determined(Declared):
    """
    Class representing the `Determined` entity, which inherits from:
    - Declared

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dc5dee4e_4305_4a21_8dd5_4e8311c98c73'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Determined'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Determined(
    
    class_iri='https://w3id.org/emmo#EMMO_dc5dee4e_4305_4a21_8dd5_4e8311c98c73',
    
    class_name='Determined',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dc5dee4e_4305_4a21_8dd5_4e8311c98c73',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Determined',
        alias="class_name"
    )
    

    
    

    

    