
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ArithmeticOperatorModule import ArithmeticOperator







class Plus(ArithmeticOperator):
    """
    Class representing the `Plus` entity, which inherits from:
    - ArithmeticOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8de14a59_660b_454f_aff8_76a07ce185f4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Plus'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Plus(
    
    class_iri='https://w3id.org/emmo#EMMO_8de14a59_660b_454f_aff8_76a07ce185f4',
    
    class_name='Plus',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8de14a59_660b_454f_aff8_76a07ce185f4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Plus',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    