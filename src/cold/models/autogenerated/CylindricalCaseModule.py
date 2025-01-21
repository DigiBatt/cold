
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RoundCaseModule import RoundCase







class CylindricalCase(RoundCase):
    """
    Class representing the `CylindricalCase` entity, which inherits from:
    - RoundCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b1cf9fee_2164_4f95_8204_90f717373a8a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CylindricalCase'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CylindricalCase(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b1cf9fee_2164_4f95_8204_90f717373a8a',
    
    class_name='CylindricalCase',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b1cf9fee_2164_4f95_8204_90f717373a8a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CylindricalCase',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    