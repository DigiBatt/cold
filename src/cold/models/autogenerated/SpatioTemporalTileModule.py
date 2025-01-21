
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TileModule import Tile







class SpatioTemporalTile(Tile):
    """
    Class representing the `SpatioTemporalTile` entity, which inherits from:
    - Tile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2e46d966_9f14_4673_821e_7c7cf2957926'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpatioTemporalTile'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpatioTemporalTile(
    
    class_iri='https://w3id.org/emmo#EMMO_2e46d966_9f14_4673_821e_7c7cf2957926',
    
    class_name='SpatioTemporalTile',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2e46d966_9f14_4673_821e_7c7cf2957926',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpatioTemporalTile',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    