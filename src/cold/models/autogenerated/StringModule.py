
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SymbolicConstructModule import SymbolicConstruct







class String(SymbolicConstruct):
    """
    Class representing the `String` entity, which inherits from:
    - SymbolicConstruct

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_50ea1ec5_f157_41b0_b46b_a9032f17ca10'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'String'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = String(
    
    class_iri='https://w3id.org/emmo#EMMO_50ea1ec5_f157_41b0_b46b_a9032f17ca10',
    
    class_name='String',
    
    elucidation="example_value",
    
    comment="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_50ea1ec5_f157_41b0_b46b_a9032f17ca10',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'String',
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
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    