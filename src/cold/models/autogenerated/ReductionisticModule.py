
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerspectiveModule import Perspective







class Reductionistic(Perspective):
    """
    Class representing the `Reductionistic` entity, which inherits from:
    - Perspective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_15db234d_ecaf_4715_9838_4b4ec424fb13'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Reductionistic'`
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
    obj = Reductionistic(
    
    class_iri='https://w3id.org/emmo#EMMO_15db234d_ecaf_4715_9838_4b4ec424fb13',
    
    class_name='Reductionistic',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_15db234d_ecaf_4715_9838_4b4ec424fb13',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Reductionistic',
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
    

    
    

    

    