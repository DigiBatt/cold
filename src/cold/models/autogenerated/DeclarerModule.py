
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InterpreterModule import Interpreter







class Declarer(Interpreter):
    """
    Class representing the `Declarer` entity, which inherits from:
    - Interpreter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2d72e38c_d587_437f_98f6_f2718fb130eb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Declarer'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Declarer(
    
    class_iri='https://w3id.org/emmo#EMMO_2d72e38c_d587_437f_98f6_f2718fb130eb',
    
    class_name='Declarer',
    
    example="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2d72e38c_d587_437f_98f6_f2718fb130eb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Declarer',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    