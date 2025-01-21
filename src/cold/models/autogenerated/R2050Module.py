
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoinCaseModule import CoinCase







class R2050(CoinCase):
    """
    Class representing the `R2050` entity, which inherits from:
    - CoinCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_400cb3e0_27b5_4d9a_be80_f86ad2757763'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R2050'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R2050(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_400cb3e0_27b5_4d9a_be80_f86ad2757763',
    
    class_name='R2050',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_400cb3e0_27b5_4d9a_be80_f86ad2757763',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R2050',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    