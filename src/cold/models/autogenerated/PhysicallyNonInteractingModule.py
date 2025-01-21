
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalSystemModule import CausalSystem







class PhysicallyNonInteracting(CausalSystem):
    """
    Class representing the `PhysicallyNonInteracting` entity, which inherits from:
    - CausalSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0f19d84e_05b4_47c9_a5de_bb2a913d211b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicallyNonInteracting'`
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
    obj = PhysicallyNonInteracting(
    
    class_iri='https://w3id.org/emmo#EMMO_0f19d84e_05b4_47c9_a5de_bb2a913d211b',
    
    class_name='PhysicallyNonInteracting',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0f19d84e_05b4_47c9_a5de_bb2a913d211b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicallyNonInteracting',
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
    

    
    

    

    