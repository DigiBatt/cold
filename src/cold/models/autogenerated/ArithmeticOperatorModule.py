
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlgebricOperatorModule import AlgebricOperator







class ArithmeticOperator(AlgebricOperator):
    """
    Class representing the `ArithmeticOperator` entity, which inherits from:
    - AlgebricOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_707f0cd1_941c_4b57_9f20_d0ba30cd6ff3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ArithmeticOperator'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ArithmeticOperator(
    
    class_iri='https://w3id.org/emmo#EMMO_707f0cd1_941c_4b57_9f20_d0ba30cd6ff3',
    
    class_name='ArithmeticOperator',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_707f0cd1_941c_4b57_9f20_d0ba30cd6ff3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ArithmeticOperator',
        alias="class_name"
    )
    

    
    

    

    