
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InterpreterModule import Interpreter







class Cogniser(Interpreter):
    """
    Class representing the `Cogniser` entity, which inherits from:
    - Interpreter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_19608340_178c_4bfd_bd4d_0d3b935c6fec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Cogniser'`
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
    obj = Cogniser(
    
    class_iri='https://w3id.org/emmo#EMMO_19608340_178c_4bfd_bd4d_0d3b935c6fec',
    
    class_name='Cogniser',
    
    example="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_19608340_178c_4bfd_bd4d_0d3b935c6fec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Cogniser',
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
    

    
    

    

    