
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ColloidModule import Colloid







class Sol(Colloid):
    """
    Class representing the `Sol` entity, which inherits from:
    - Colloid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_31557fae_b039_491c_bcbb_0ccb8711d5a6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Sol'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Sol(
    
    class_iri='https://w3id.org/emmo#EMMO_31557fae_b039_491c_bcbb_0ccb8711d5a6',
    
    class_name='Sol',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_31557fae_b039_491c_bcbb_0ccb8711d5a6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Sol',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    