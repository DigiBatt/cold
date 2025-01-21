
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalSymbolModule import MathematicalSymbol



from .MathematicalModule import Mathematical



from .SymbolModule import Symbol







class Equals(MathematicalSymbol, Mathematical, Symbol):
    """
    Class representing the `Equals` entity, which inherits from:
    - MathematicalSymbol, Mathematical, Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_535d75a4_1972_40bc_88c6_ca566386934f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Equals'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Equals(
    
    class_iri='https://w3id.org/emmo#EMMO_535d75a4_1972_40bc_88c6_ca566386934f',
    
    class_name='Equals',
    
    hasSymbolValue="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_535d75a4_1972_40bc_88c6_ca566386934f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Equals',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    