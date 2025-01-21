
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemporalTilingModule import TemporalTiling







class Join(TemporalTiling):
    """
    Class representing the `Join` entity, which inherits from:
    - TemporalTiling

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c7ee175d_4c25_45cb_b74e_71435b11b77d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Join'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Join(
    
    class_iri='https://w3id.org/emmo#EMMO_c7ee175d_4c25_45cb_b74e_71435b11b77d',
    
    class_name='Join',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c7ee175d_4c25_45cb_b74e_71435b11b77d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Join',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    