
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTileModule import SpatioTemporalTile



from .TaskModule import Task



from .TileModule import Tile







class Step(SpatioTemporalTile, Task, Tile):
    """
    Class representing the `Step` entity, which inherits from:
    - SpatioTemporalTile, Task, Tile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9f6ec830_c59f_46aa_8a22_945ba20b6ea3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Step'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Step(
    
    class_iri='https://w3id.org/emmo#EMMO_9f6ec830_c59f_46aa_8a22_945ba20b6ea3',
    
    class_name='Step',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9f6ec830_c59f_46aa_8a22_945ba20b6ea3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Step',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    