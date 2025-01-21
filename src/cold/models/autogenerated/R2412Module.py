
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoinCaseModule import CoinCase







class R2412(CoinCase):
    """
    Class representing the `R2412` entity, which inherits from:
    - CoinCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a4e7c3d6_45bd_402a_962f_5d4b88af84ff'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R2412'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R2412(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a4e7c3d6_45bd_402a_962f_5d4b88af84ff',
    
    class_name='R2412',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a4e7c3d6_45bd_402a_962f_5d4b88af84ff',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R2412',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    