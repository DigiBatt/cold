
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalElementModule import ChemicalElement







class NeonSymbol(ChemicalElement):
    """
    Class representing the `NeonSymbol` entity, which inherits from:
    - ChemicalElement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2e96348b_f8d1_5877_a5c5_b6863c5ebcf2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NeonSymbol'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NeonSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_2e96348b_f8d1_5877_a5c5_b6863c5ebcf2',
    
    class_name='NeonSymbol',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2e96348b_f8d1_5877_a5c5_b6863c5ebcf2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NeonSymbol',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    