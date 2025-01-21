
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalModule import Mathematical







class Variable(Mathematical):
    """
    Class representing the `Variable` entity, which inherits from:
    - Mathematical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1eed0732_e3f1_4b2c_a9c4_b4e75eeb5895'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Variable'`
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
    obj = Variable(
    
    class_iri='https://w3id.org/emmo#EMMO_1eed0732_e3f1_4b2c_a9c4_b4e75eeb5895',
    
    class_name='Variable',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1eed0732_e3f1_4b2c_a9c4_b4e75eeb5895',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Variable',
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
    

    
    

    

    