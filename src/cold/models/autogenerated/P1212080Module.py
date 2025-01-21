
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrismaticCaseModule import PrismaticCase







class P1212080(PrismaticCase):
    """
    Class representing the `P1212080` entity, which inherits from:
    - PrismaticCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c54fbb75_0528_49c0_97e0_258798a947e4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'P1212080'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = P1212080(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c54fbb75_0528_49c0_97e0_258798a947e4',
    
    class_name='P1212080',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c54fbb75_0528_49c0_97e0_258798a947e4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'P1212080',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    