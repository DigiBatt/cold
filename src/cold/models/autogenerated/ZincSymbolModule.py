
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalElementModule import ChemicalElement







class ZincSymbol(ChemicalElement):
    """
    Class representing the `ZincSymbol` entity, which inherits from:
    - ChemicalElement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0bd0c81a_2972_5b2d_8ff5_bb72a82b9c0d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincSymbol'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_0bd0c81a_2972_5b2d_8ff5_bb72a82b9c0d',
    
    class_name='ZincSymbol',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0bd0c81a_2972_5b2d_8ff5_bb72a82b9c0d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincSymbol',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    