
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalModule import Mathematical



from .SymbolModule import Symbol







class MathematicalSymbol(Mathematical, Symbol):
    """
    Class representing the `MathematicalSymbol` entity, which inherits from:
    - Mathematical, Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5be83f9c_a4ba_4b9a_be1a_5bfc6e891231'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MathematicalSymbol'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MathematicalSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_5be83f9c_a4ba_4b9a_be1a_5bfc6e891231',
    
    class_name='MathematicalSymbol',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5be83f9c_a4ba_4b9a_be1a_5bfc6e891231',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MathematicalSymbol',
        alias="class_name"
    )
    

    
    

    

    