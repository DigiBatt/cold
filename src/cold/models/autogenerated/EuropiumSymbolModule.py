
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalElementModule import ChemicalElement







class EuropiumSymbol(ChemicalElement):
    """
    Class representing the `EuropiumSymbol` entity, which inherits from:
    - ChemicalElement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4894a40d_6bf5_54a2_8b21_e9b278e0e973'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EuropiumSymbol'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EuropiumSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_4894a40d_6bf5_54a2_8b21_e9b278e0e973',
    
    class_name='EuropiumSymbol',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4894a40d_6bf5_54a2_8b21_e9b278e0e973',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EuropiumSymbol',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    