
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuantityModule import Quantity



from .ObjectiveModule import Objective







class ObjectiveProperty(Quantity, Objective):
    """
    Class representing the `ObjectiveProperty` entity, which inherits from:
    - Quantity, Objective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dd4a7f3e_ef56_466c_ac1a_d2716b5f87ec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ObjectiveProperty'`
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
    obj = ObjectiveProperty(
    
    class_iri='https://w3id.org/emmo#EMMO_dd4a7f3e_ef56_466c_ac1a_d2716b5f87ec',
    
    class_name='ObjectiveProperty',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dd4a7f3e_ef56_466c_ac1a_d2716b5f87ec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ObjectiveProperty',
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
    

    
    

    

    