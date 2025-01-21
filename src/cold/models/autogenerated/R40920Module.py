
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CylindricalCaseModule import CylindricalCase







class R40920(CylindricalCase):
    """
    Class representing the `R40920` entity, which inherits from:
    - CylindricalCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6eaa3c0d_e1f3_4c6e_91a6_9b8c5a21b8cb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R40920'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R40920(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6eaa3c0d_e1f3_4c6e_91a6_9b8c5a21b8cb',
    
    class_name='R40920',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_6eaa3c0d_e1f3_4c6e_91a6_9b8c5a21b8cb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R40920',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    