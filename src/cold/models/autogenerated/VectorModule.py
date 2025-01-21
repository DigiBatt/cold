
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ArrayModule import Array



from .SpatioTemporalTessellationModule import SpatioTemporalTessellation



from .MathematicalConstructModule import MathematicalConstruct





from .SpatialTileModule import SpatialTile





class Vector(Array, SpatioTemporalTessellation, MathematicalConstruct):
    """
    Class representing the `Vector` entity, which inherits from:
    - Array, SpatioTemporalTessellation, MathematicalConstruct

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_06658d8d_dcde_4fc9_aae1_17f71c0bcdec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Vector'`
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
    obj = Vector(
    
    class_iri='https://w3id.org/emmo#EMMO_06658d8d_dcde_4fc9_aae1_17f71c0bcdec',
    
    class_name='Vector',
    
    hasSpatialTile="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_06658d8d_dcde_4fc9_aae1_17f71c0bcdec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Vector',
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
    
    

    

    