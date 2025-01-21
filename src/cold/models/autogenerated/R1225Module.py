
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoinCaseModule import CoinCase







class R1225(CoinCase):
    """
    Class representing the `R1225` entity, which inherits from:
    - CoinCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f7e253da_b12e_40b0_ba51_8cb039839ab6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R1225'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R1225(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f7e253da_b12e_40b0_ba51_8cb039839ab6',
    
    class_name='R1225',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f7e253da_b12e_40b0_ba51_8cb039839ab6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R1225',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    