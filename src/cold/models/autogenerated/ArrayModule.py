
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalModule import Mathematical







class Array(Mathematical):
    """
    Class representing the `Array` entity, which inherits from:
    - Mathematical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_28fbea28_2204_4613_87ff_6d877b855fcd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Array'`
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
    obj = Array(
    
    class_iri='https://w3id.org/emmo#EMMO_28fbea28_2204_4613_87ff_6d877b855fcd',
    
    class_name='Array',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_28fbea28_2204_4613_87ff_6d877b855fcd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Array',
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
    

    
    

    

    