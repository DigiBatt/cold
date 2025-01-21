
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ExpressionModule import Expression







class AlgebricExpression(Expression):
    """
    Class representing the `AlgebricExpression` entity, which inherits from:
    - Expression

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1aed91a3_d00c_48af_8f43_a0c958b2512a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlgebricExpression'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlgebricExpression(
    
    class_iri='https://w3id.org/emmo#EMMO_1aed91a3_d00c_48af_8f43_a0c958b2512a',
    
    class_name='AlgebricExpression',
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1aed91a3_d00c_48af_8f43_a0c958b2512a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlgebricExpression',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    