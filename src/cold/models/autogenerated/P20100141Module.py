
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrismaticCaseModule import PrismaticCase







class P20100141(PrismaticCase):
    """
    Class representing the `P20100141` entity, which inherits from:
    - PrismaticCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bba6b94e_c0d7_40bf_a9d6_413ff458397c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'P20100141'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = P20100141(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bba6b94e_c0d7_40bf_a9d6_413ff458397c',
    
    class_name='P20100141',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bba6b94e_c0d7_40bf_a9d6_413ff458397c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'P20100141',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    