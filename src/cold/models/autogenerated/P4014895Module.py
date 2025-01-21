
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PrismaticCaseModule import PrismaticCase







class P4014895(PrismaticCase):
    """
    Class representing the `P4014895` entity, which inherits from:
    - PrismaticCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_41ab11ec_af9f_401d_b80d_474c1dc86cd6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'P4014895'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = P4014895(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_41ab11ec_af9f_401d_b80d_474c1dc86cd6',
    
    class_name='P4014895',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_41ab11ec_af9f_401d_b80d_474c1dc86cd6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'P4014895',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    