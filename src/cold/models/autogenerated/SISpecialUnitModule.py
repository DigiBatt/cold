
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIUnitSymbolModule import SIUnitSymbol



from .SpecialUnitModule import SpecialUnit







class SISpecialUnit(SIUnitSymbol, SpecialUnit):
    """
    Class representing the `SISpecialUnit` entity, which inherits from:
    - SIUnitSymbol, SpecialUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e9ffc696_5228_4ff9_8a60_0f5e05e9931b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SISpecialUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SISpecialUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_e9ffc696_5228_4ff9_8a60_0f5e05e9931b',
    
    class_name='SISpecialUnit',
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e9ffc696_5228_4ff9_8a60_0f5e05e9931b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SISpecialUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    