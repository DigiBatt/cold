
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlgebricExpressionModule import AlgebricExpression







class ArithmeticExpression(AlgebricExpression):
    """
    Class representing the `ArithmeticExpression` entity, which inherits from:
    - AlgebricExpression

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_89083bab_f69c_4d06_bf6d_62973b56cdc7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ArithmeticExpression'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ArithmeticExpression(
    
    class_iri='https://w3id.org/emmo#EMMO_89083bab_f69c_4d06_bf6d_62973b56cdc7',
    
    class_name='ArithmeticExpression',
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_89083bab_f69c_4d06_bf6d_62973b56cdc7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ArithmeticExpression',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    