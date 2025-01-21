
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrismaticCaseModule import PrismaticCase







class P2714898(PrismaticCase):
    """
    Class representing the `P2714898` entity, which inherits from:
    - PrismaticCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50d9652c_6b68_457c_bd72_f89a8e549bcf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'P2714898'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = P2714898(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50d9652c_6b68_457c_bd72_f89a8e549bcf',
    
    class_name='P2714898',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50d9652c_6b68_457c_bd72_f89a8e549bcf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'P2714898',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    