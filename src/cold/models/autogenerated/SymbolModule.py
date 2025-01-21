
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolicModule import Symbolic







class Symbol(Symbolic):
    """
    Class representing the `Symbol` entity, which inherits from:
    - Symbolic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a1083d0a_c1fb_471f_8e20_a98f881ad527'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Symbol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Symbol(
    
    class_iri='https://w3id.org/emmo#EMMO_a1083d0a_c1fb_471f_8e20_a98f881ad527',
    
    class_name='Symbol',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a1083d0a_c1fb_471f_8e20_a98f881ad527',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Symbol',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    