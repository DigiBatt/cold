
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ArithmeticOperatorModule import ArithmeticOperator







class Division(ArithmeticOperator):
    """
    Class representing the `Division` entity, which inherits from:
    - ArithmeticOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a365b3c1_7bde_41d7_a15b_2820762e85f4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Division'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Division(
    
    class_iri='https://w3id.org/emmo#EMMO_a365b3c1_7bde_41d7_a15b_2820762e85f4',
    
    class_name='Division',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a365b3c1_7bde_41d7_a15b_2820762e85f4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Division',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    