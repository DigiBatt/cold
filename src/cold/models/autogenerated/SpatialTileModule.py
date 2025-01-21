
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTileModule import SpatioTemporalTile







class SpatialTile(SpatioTemporalTile):
    """
    Class representing the `SpatialTile` entity, which inherits from:
    - SpatioTemporalTile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4cf484af_082a_40f5_9f11_930bf4634482'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SpatialTile'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SpatialTile(
    
    class_iri='https://w3id.org/emmo#EMMO_4cf484af_082a_40f5_9f11_930bf4634482',
    
    class_name='SpatialTile',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4cf484af_082a_40f5_9f11_930bf4634482',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SpatialTile',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    