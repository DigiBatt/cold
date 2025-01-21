
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DefiningEquationModule import DefiningEquation







class MathematicalFunction(DefiningEquation):
    """
    Class representing the `MathematicalFunction` entity, which inherits from:
    - DefiningEquation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4bc29b0f_8fcc_4026_a291_f9774a66d9b8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MathematicalFunction'`
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
    obj = MathematicalFunction(
    
    class_iri='https://w3id.org/emmo#EMMO_4bc29b0f_8fcc_4026_a291_f9774a66d9b8',
    
    class_name='MathematicalFunction',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4bc29b0f_8fcc_4026_a291_f9774a66d9b8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MathematicalFunction',
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
    

    
    

    

    