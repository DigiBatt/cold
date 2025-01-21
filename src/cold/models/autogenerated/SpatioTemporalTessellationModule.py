
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TessellationModule import Tessellation





from .SpatioTemporalTileModule import SpatioTemporalTile





class SpatioTemporalTessellation(Tessellation):
    """
    Class representing the `SpatioTemporalTessellation` entity, which inherits from:
    - Tessellation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e12dcfa4_c9f1_4546_9a12_8457c052e6ba'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpatioTemporalTessellation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSpatioTemporalTile` (`Optional[SpatioTemporalTile]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatioTemporalTile`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpatioTemporalTessellation(
    
    class_iri='https://w3id.org/emmo#EMMO_e12dcfa4_c9f1_4546_9a12_8457c052e6ba',
    
    class_name='SpatioTemporalTessellation',
    
    elucidation="example_value",
    
    hasSpatioTemporalTile="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e12dcfa4_c9f1_4546_9a12_8457c052e6ba',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpatioTemporalTessellation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasSpatioTemporalTile: Optional[SpatioTemporalTile] = Field(
        None,
        alias="hasSpatioTemporalTile"
    )
    

    
    @validator("hasSpatioTemporalTile", pre=True, always=True)
    def validate_hasSpatioTemporalTile(cls, value):
        if value is not None and not isinstance(value, SpatioTemporalTile):
            raise ValueError(f"Field 'hasSpatioTemporalTile' must be an instance of 'SpatioTemporalTile' or its subclass.")
        return value
    
    

    

    