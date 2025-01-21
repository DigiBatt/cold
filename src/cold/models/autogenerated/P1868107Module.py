
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrismaticCaseModule import PrismaticCase







class P1868107(PrismaticCase):
    """
    Class representing the `P1868107` entity, which inherits from:
    - PrismaticCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d1bf3cdd_d618_40e3_b055_a952ef632157'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'P1868107'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = P1868107(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d1bf3cdd_d618_40e3_b055_a952ef632157',
    
    class_name='P1868107',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d1bf3cdd_d618_40e3_b055_a952ef632157',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'P1868107',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    