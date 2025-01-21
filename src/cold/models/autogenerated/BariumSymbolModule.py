
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalElementModule import ChemicalElement







class BariumSymbol(ChemicalElement):
    """
    Class representing the `BariumSymbol` entity, which inherits from:
    - ChemicalElement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d60619c8_1abe_52c0_9491_eb3086245e22'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumSymbol'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_d60619c8_1abe_52c0_9491_eb3086245e22',
    
    class_name='BariumSymbol',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d60619c8_1abe_52c0_9491_eb3086245e22',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumSymbol',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    