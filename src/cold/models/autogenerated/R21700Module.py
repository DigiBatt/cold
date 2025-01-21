
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CylindricalCaseModule import CylindricalCase







class R21700(CylindricalCase):
    """
    Class representing the `R21700` entity, which inherits from:
    - CylindricalCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3b048a62_8591_4bf1_8fac_3d647beb9323'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R21700'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R21700(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3b048a62_8591_4bf1_8fac_3d647beb9323',
    
    class_name='R21700',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3b048a62_8591_4bf1_8fac_3d647beb9323',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R21700',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    