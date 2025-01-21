
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoinCaseModule import CoinCase







class R2330(CoinCase):
    """
    Class representing the `R2330` entity, which inherits from:
    - CoinCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_11579b47_cbf8_45ac_aed3_343ea533b346'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R2330'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R2330(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_11579b47_cbf8_45ac_aed3_343ea533b346',
    
    class_name='R2330',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_11579b47_cbf8_45ac_aed3_343ea533b346',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R2330',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    