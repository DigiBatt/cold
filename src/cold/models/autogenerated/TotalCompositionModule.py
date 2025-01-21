
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalCompositionModule import ChemicalComposition





from .SpatialTileModule import SpatialTile





class TotalComposition(ChemicalComposition):
    """
    Class representing the `TotalComposition` entity, which inherits from:
    - ChemicalComposition

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0eabfde6_c6c5_4b1f_bf10_e4e0e06e9b2e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TotalComposition'`
        - **Alias**: `class_name`
    
    - `hasSpatialTile` (`Optional[SpatialTile]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialTile`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TotalComposition(
    
    class_iri='https://w3id.org/emmo#EMMO_0eabfde6_c6c5_4b1f_bf10_e4e0e06e9b2e',
    
    class_name='TotalComposition',
    
    hasSpatialTile="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0eabfde6_c6c5_4b1f_bf10_e4e0e06e9b2e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TotalComposition',
        alias="class_name"
    )
    
    hasSpatialTile: Optional[SpatialTile] = Field(
        None,
        alias="hasSpatialTile"
    )
    

    
    @validator("hasSpatialTile", pre=True, always=True)
    def validate_hasSpatialTile(cls, value):
        if value is not None and not isinstance(value, SpatialTile):
            raise ValueError(f"Field 'hasSpatialTile' must be an instance of 'SpatialTile' or its subclass.")
        return value
    
    

    

    