
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SignModule import Sign







class Index(Sign):
    """
    Class representing the `Index` entity, which inherits from:
    - Sign

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0cd58641_824c_4851_907f_f4c3be76630c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Index'`
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
    obj = Index(
    
    class_iri='https://w3id.org/emmo#EMMO_0cd58641_824c_4851_907f_f4c3be76630c',
    
    class_name='Index',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0cd58641_824c_4851_907f_f4c3be76630c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Index',
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
    

    
    

    

    