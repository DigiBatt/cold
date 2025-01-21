
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTileModule import SpatioTemporalTile







class TemporalTile(SpatioTemporalTile):
    """
    Class representing the `TemporalTile` entity, which inherits from:
    - SpatioTemporalTile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_504ad89e_dd4a_4fa6_aeb6_15c8ce0cde9b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemporalTile'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemporalTile(
    
    class_iri='https://w3id.org/emmo#EMMO_504ad89e_dd4a_4fa6_aeb6_15c8ce0cde9b',
    
    class_name='TemporalTile',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_504ad89e_dd4a_4fa6_aeb6_15c8ce0cde9b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemporalTile',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    