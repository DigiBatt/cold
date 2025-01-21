
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ArithmeticOperatorModule import ArithmeticOperator







class Multiplication(ArithmeticOperator):
    """
    Class representing the `Multiplication` entity, which inherits from:
    - ArithmeticOperator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2b1303e8_d4c3_453b_9918_76f1d009543f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Multiplication'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Multiplication(
    
    class_iri='https://w3id.org/emmo#EMMO_2b1303e8_d4c3_453b_9918_76f1d009543f',
    
    class_name='Multiplication',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2b1303e8_d4c3_453b_9918_76f1d009543f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Multiplication',
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    

    
    

    

    