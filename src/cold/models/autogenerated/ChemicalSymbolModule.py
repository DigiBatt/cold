
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolModule import Symbol



from .ChemicalModule import Chemical







class ChemicalSymbol(Symbol, Chemical):
    """
    Class representing the `ChemicalSymbol` entity, which inherits from:
    - Symbol, Chemical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d357e0dd_3497_4590_af6f_7954db7fecf7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalSymbol'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicalSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_d357e0dd_3497_4590_af6f_7954db7fecf7',
    
    class_name='ChemicalSymbol',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d357e0dd_3497_4590_af6f_7954db7fecf7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalSymbol',
        alias="class_name"
    )
    

    
    

    

    