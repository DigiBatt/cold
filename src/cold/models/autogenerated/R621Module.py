
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoinCaseModule import CoinCase







class R621(CoinCase):
    """
    Class representing the `R621` entity, which inherits from:
    - CoinCase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_15ec346a_6d3c_4161_95e1_9cf889965f85'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'R621'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = R621(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_15ec346a_6d3c_4161_95e1_9cf889965f85',
    
    class_name='R621',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_15ec346a_6d3c_4161_95e1_9cf889965f85',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'R621',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    