
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComponentModule import Component







class CatholyteTank(Component):
    """
    Class representing the `CatholyteTank` entity, which inherits from:
    - Component

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9b6853e7_3412_463d_b5a9_82c14acebf7d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CatholyteTank'`
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
    obj = CatholyteTank(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9b6853e7_3412_463d_b5a9_82c14acebf7d',
    
    class_name='CatholyteTank',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9b6853e7_3412_463d_b5a9_82c14acebf7d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CatholyteTank',
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
    

    
    

    

    