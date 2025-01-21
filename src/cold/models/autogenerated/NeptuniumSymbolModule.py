
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalElementModule import ChemicalElement







class NeptuniumSymbol(ChemicalElement):
    """
    Class representing the `NeptuniumSymbol` entity, which inherits from:
    - ChemicalElement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e941986d_658b_5a08_ae3d_4cc170344b06'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NeptuniumSymbol'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NeptuniumSymbol(
    
    class_iri='https://w3id.org/emmo#EMMO_e941986d_658b_5a08_ae3d_4cc170344b06',
    
    class_name='NeptuniumSymbol',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e941986d_658b_5a08_ae3d_4cc170344b06',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NeptuniumSymbol',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    