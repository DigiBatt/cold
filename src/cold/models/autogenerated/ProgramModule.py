
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SoftwareModule import Software







class Program(Software):
    """
    Class representing the `Program` entity, which inherits from:
    - Software

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_65411b3d_c8d3_4111_86a9_a2ce0a64c647'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Program'`
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
    obj = Program(
    
    class_iri='https://w3id.org/emmo#EMMO_65411b3d_c8d3_4111_86a9_a2ce0a64c647',
    
    class_name='Program',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_65411b3d_c8d3_4111_86a9_a2ce0a64c647',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Program',
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
    

    
    

    

    