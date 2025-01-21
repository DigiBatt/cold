
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolModule import Symbol







class Letter(Symbol):
    """
    Class representing the `Letter` entity, which inherits from:
    - Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_bed2fe4c_dc7e_43a8_8200_6aac44030bff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Letter'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Letter(
    
    class_iri='https://w3id.org/emmo#EMMO_bed2fe4c_dc7e_43a8_8200_6aac44030bff',
    
    class_name='Letter',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_bed2fe4c_dc7e_43a8_8200_6aac44030bff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Letter',
        alias="class_name"
    )
    

    
    

    

    