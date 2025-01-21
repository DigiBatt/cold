
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolicModule import Symbolic







class SymbolicConstruct(Symbolic):
    """
    Class representing the `SymbolicConstruct` entity, which inherits from:
    - Symbolic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_89a0c87c_0804_4013_937a_6fe234d9499c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SymbolicConstruct'`
        - **Alias**: `class_name`
    
    - `hasProperPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasProperPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SymbolicConstruct(
    
    class_iri='https://w3id.org/emmo#EMMO_89a0c87c_0804_4013_937a_6fe234d9499c',
    
    class_name='SymbolicConstruct',
    
    hasProperPart="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_89a0c87c_0804_4013_937a_6fe234d9499c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SymbolicConstruct',
        alias="class_name"
    )
    
    hasProperPart: Optional[str] = Field(
        None,
        alias="hasProperPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    