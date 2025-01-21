
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VectorModule import Vector







class Shape3Vector(Vector):
    """
    Class representing the `Shape3Vector` entity, which inherits from:
    - Vector

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2ff07b07_c447_490f_903a_f6a72a12d7bf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Shape3Vector'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Shape3Vector(
    
    class_iri='https://w3id.org/emmo#EMMO_2ff07b07_c447_490f_903a_f6a72a12d7bf',
    
    class_name='Shape3Vector',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2ff07b07_c447_490f_903a_f6a72a12d7bf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Shape3Vector',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    