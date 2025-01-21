
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalCompositionModule import ChemicalComposition





from .SpatialTileModule import SpatialTile





class SingleComponentComposition(ChemicalComposition):
    """
    Class representing the `SingleComponentComposition` entity, which inherits from:
    - ChemicalComposition

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_172e2c96_180b_40f8_a3e7_b624471f40c2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SingleComponentComposition'`
        - **Alias**: `class_name`
    
    - `hasSpatialTile` (`Optional[SpatialTile]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialTile`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SingleComponentComposition(
    
    class_iri='https://w3id.org/emmo#EMMO_172e2c96_180b_40f8_a3e7_b624471f40c2',
    
    class_name='SingleComponentComposition',
    
    hasSpatialTile="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_172e2c96_180b_40f8_a3e7_b624471f40c2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SingleComponentComposition',
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
    
    

    

    