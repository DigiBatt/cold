
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation





from .TileModule import Tile





class MixedTiling(SpatioTemporalTessellation):
    """
    Class representing the `MixedTiling` entity, which inherits from:
    - SpatioTemporalTessellation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2b1fb71c_0eb0_445c_9be7_fb5d30ae79fd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MixedTiling'`
        - **Alias**: `class_name`
    
    - `hasDirectPart` (`Optional[Tile]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDirectPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MixedTiling(
    
    class_iri='https://w3id.org/emmo#EMMO_2b1fb71c_0eb0_445c_9be7_fb5d30ae79fd',
    
    class_name='MixedTiling',
    
    hasDirectPart="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2b1fb71c_0eb0_445c_9be7_fb5d30ae79fd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MixedTiling',
        alias="class_name"
    )
    
    hasDirectPart: Optional[Tile] = Field(
        None,
        alias="hasDirectPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasDirectPart", pre=True, always=True)
    def validate_hasDirectPart(cls, value):
        if value is not None and not isinstance(value, Tile):
            raise ValueError(f"Field 'hasDirectPart' must be an instance of 'Tile' or its subclass.")
        return value
    
    

    

    