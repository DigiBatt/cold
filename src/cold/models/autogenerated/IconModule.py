
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SignModule import Sign







class Icon(Sign):
    """
    Class representing the `Icon` entity, which inherits from:
    - Sign

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d7788d1a_020d_4c78_85a1_13563fcec168'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Icon'`
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
    obj = Icon(
    
    class_iri='https://w3id.org/emmo#EMMO_d7788d1a_020d_4c78_85a1_13563fcec168',
    
    class_name='Icon',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d7788d1a_020d_4c78_85a1_13563fcec168',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Icon',
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
    

    
    

    

    