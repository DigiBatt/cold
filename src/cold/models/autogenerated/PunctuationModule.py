
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolModule import Symbol







class Punctuation(Symbol):
    """
    Class representing the `Punctuation` entity, which inherits from:
    - Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a817035a_3e3c_4709_8ede_3205df3031a3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Punctuation'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Punctuation(
    
    class_iri='https://w3id.org/emmo#EMMO_a817035a_3e3c_4709_8ede_3205df3031a3',
    
    class_name='Punctuation',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a817035a_3e3c_4709_8ede_3205df3031a3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Punctuation',
        alias="class_name"
    )
    

    
    

    

    