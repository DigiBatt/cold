
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LiquidAerosolModule import LiquidAerosol







class Vapor(LiquidAerosol):
    """
    Class representing the `Vapor` entity, which inherits from:
    - LiquidAerosol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4d604a13_d1f6_42fd_818f_d3138d5e308c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Vapor'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Vapor(
    
    class_iri='https://w3id.org/emmo#EMMO_4d604a13_d1f6_42fd_818f_d3138d5e308c',
    
    class_name='Vapor',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4d604a13_d1f6_42fd_818f_d3138d5e308c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Vapor',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    