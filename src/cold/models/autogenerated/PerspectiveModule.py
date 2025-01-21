
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalStructureModule import CausalStructure







class Perspective(CausalStructure):
    """
    Class representing the `Perspective` entity, which inherits from:
    - CausalStructure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_49267eba_5548_4163_8f36_518d65b583f9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Perspective'`
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
    obj = Perspective(
    
    class_iri='https://w3id.org/emmo#EMMO_49267eba_5548_4163_8f36_518d65b583f9',
    
    class_name='Perspective',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_49267eba_5548_4163_8f36_518d65b583f9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Perspective',
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
    

    
    

    

    