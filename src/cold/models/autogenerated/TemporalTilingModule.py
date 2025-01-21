
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation







class TemporalTiling(SpatioTemporalTessellation):
    """
    Class representing the `TemporalTiling` entity, which inherits from:
    - SpatioTemporalTessellation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f7f41d20_eabb_4bcb_9a16_0436851fcd5c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemporalTiling'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemporalTiling(
    
    class_iri='https://w3id.org/emmo#EMMO_f7f41d20_eabb_4bcb_9a16_0436851fcd5c',
    
    class_name='TemporalTiling',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f7f41d20_eabb_4bcb_9a16_0436851fcd5c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemporalTiling',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    