
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation



from .OverpotentialModule import Overpotential





from .SpatialTileModule import SpatialTile





class SurfaceOverpotential(SpatioTemporalTessellation, Overpotential):
    """
    Class representing the `SurfaceOverpotential` entity, which inherits from:
    - SpatioTemporalTessellation, Overpotential

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_60741c58_a10d_4aa6_bb68_0066a6ff8e30'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SurfaceOverpotential'`
        - **Alias**: `class_name`
    
    - `hasSpatialTile` (`Optional[SpatialTile]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialTile`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SurfaceOverpotential(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_60741c58_a10d_4aa6_bb68_0066a6ff8e30',
    
    class_name='SurfaceOverpotential',
    
    hasSpatialTile="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_60741c58_a10d_4aa6_bb68_0066a6ff8e30',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SurfaceOverpotential',
        alias="class_name"
    )
    
    hasSpatialTile: Optional[SpatialTile] = Field(
        None,
        alias="hasSpatialTile"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasSpatialTile", pre=True, always=True)
    def validate_hasSpatialTile(cls, value):
        if value is not None and not isinstance(value, SpatialTile):
            raise ValueError(f"Field 'hasSpatialTile' must be an instance of 'SpatialTile' or its subclass.")
        return value
    
    

    

    