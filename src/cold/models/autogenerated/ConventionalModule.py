
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SignModule import Sign







class Conventional(Sign):
    """
    Class representing the `Conventional` entity, which inherits from:
    - Sign

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_35d2e130_6e01_41ed_94f7_00b333d46cf9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Conventional'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Conventional(
    
    class_iri='https://w3id.org/emmo#EMMO_35d2e130_6e01_41ed_94f7_00b333d46cf9',
    
    class_name='Conventional',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_35d2e130_6e01_41ed_94f7_00b333d46cf9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Conventional',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    