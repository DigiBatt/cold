
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CylindricalCaseModule import CylindricalCase







class R32700(CylindricalCase):
    """
    Class representing the `R32700` entity, which inherits from:
    - CylindricalCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ad9cdad6_66e8_471e_a7c6_b79f37c20814'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R32700'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R32700(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ad9cdad6_66e8_471e_a7c6_b79f37c20814',
    
    class_name='R32700',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ad9cdad6_66e8_471e_a7c6_b79f37c20814',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R32700',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    