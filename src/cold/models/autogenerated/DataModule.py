
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerspectiveModule import Perspective







class Data(Perspective):
    """
    Class representing the `Data` entity, which inherits from:
    - Perspective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1e877c70_3b01_45a8_a8f6_8ce4f6a24660'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Data'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Data(
    
    class_iri='https://w3id.org/emmo#EMMO_1e877c70_3b01_45a8_a8f6_8ce4f6a24660',
    
    class_name='Data',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1e877c70_3b01_45a8_a8f6_8ce4f6a24660',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Data',
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
    

    
    

    

    