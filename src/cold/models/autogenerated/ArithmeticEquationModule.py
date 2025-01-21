
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EquationModule import Equation







class ArithmeticEquation(Equation):
    """
    Class representing the `ArithmeticEquation` entity, which inherits from:
    - Equation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a6138ba7_e365_4f2d_b6b4_fe5a5918d403'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ArithmeticEquation'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ArithmeticEquation(
    
    class_iri='https://w3id.org/emmo#EMMO_a6138ba7_e365_4f2d_b6b4_fe5a5918d403',
    
    class_name='ArithmeticEquation',
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a6138ba7_e365_4f2d_b6b4_fe5a5918d403',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ArithmeticEquation',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    