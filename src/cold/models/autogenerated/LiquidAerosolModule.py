
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AerosolModule import Aerosol







class LiquidAerosol(Aerosol):
    """
    Class representing the `LiquidAerosol` entity, which inherits from:
    - Aerosol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_94010cbc_c2a6_4cb9_b29a_83aa99d2ff70'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LiquidAerosol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LiquidAerosol(
    
    class_iri='https://w3id.org/emmo#EMMO_94010cbc_c2a6_4cb9_b29a_83aa99d2ff70',
    
    class_name='LiquidAerosol',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_94010cbc_c2a6_4cb9_b29a_83aa99d2ff70',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LiquidAerosol',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    