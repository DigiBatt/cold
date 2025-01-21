
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalSymbolModule import MathematicalSymbol



from .MathematicalModule import Mathematical



from .SymbolModule import Symbol







class MathematicalOperator(MathematicalSymbol, Mathematical, Symbol):
    """
    Class representing the `MathematicalOperator` entity, which inherits from:
    - MathematicalSymbol, Mathematical, Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f6d0c26a_98b6_4cf8_8632_aa259131faaa'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MathematicalOperator'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MathematicalOperator(
    
    class_iri='https://w3id.org/emmo#EMMO_f6d0c26a_98b6_4cf8_8632_aa259131faaa',
    
    class_name='MathematicalOperator',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f6d0c26a_98b6_4cf8_8632_aa259131faaa',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MathematicalOperator',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    