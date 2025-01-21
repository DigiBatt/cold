
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InterpreterModule import Interpreter







class Deducer(Interpreter):
    """
    Class representing the `Deducer` entity, which inherits from:
    - Interpreter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_36a4c1ca_5085_49ca_9e13_4c70d00c50a5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Deducer'`
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
    obj = Deducer(
    
    class_iri='https://w3id.org/emmo#EMMO_36a4c1ca_5085_49ca_9e13_4c70d00c50a5',
    
    class_name='Deducer',
    
    example="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_36a4c1ca_5085_49ca_9e13_4c70d00c50a5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Deducer',
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
    

    
    

    

    