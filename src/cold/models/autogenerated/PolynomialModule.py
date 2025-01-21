
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlgebricExpressionModule import AlgebricExpression







class Polynomial(AlgebricExpression):
    """
    Class representing the `Polynomial` entity, which inherits from:
    - AlgebricExpression

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_91447ec0_fb55_49f2_85a5_3172dff6482c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Polynomial'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Polynomial(
    
    class_iri='https://w3id.org/emmo#EMMO_91447ec0_fb55_49f2_85a5_3172dff6482c',
    
    class_name='Polynomial',
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_91447ec0_fb55_49f2_85a5_3172dff6482c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Polynomial',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    