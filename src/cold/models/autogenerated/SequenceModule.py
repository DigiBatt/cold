
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemporalTilingModule import TemporalTiling







class Sequence(TemporalTiling):
    """
    Class representing the `Sequence` entity, which inherits from:
    - TemporalTiling

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_92829beb_6ed4_4c88_bbd5_3bc7403e2895'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Sequence'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Sequence(
    
    class_iri='https://w3id.org/emmo#EMMO_92829beb_6ed4_4c88_bbd5_3bc7403e2895',
    
    class_name='Sequence',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_92829beb_6ed4_4c88_bbd5_3bc7403e2895',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Sequence',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    