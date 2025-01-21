
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CodedModule import Coded







class Description(Coded):
    """
    Class representing the `Description` entity, which inherits from:
    - Coded

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_35d4c439_fcb6_4399_a855_a89a207b41e9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Description'`
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
    obj = Description(
    
    class_iri='https://w3id.org/emmo#EMMO_35d4c439_fcb6_4399_a855_a89a207b41e9',
    
    class_name='Description',
    
    elucidation="example_value",
    
    comment="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_35d4c439_fcb6_4399_a855_a89a207b41e9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Description',
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
    

    
    

    

    