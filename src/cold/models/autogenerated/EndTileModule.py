
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTileModule import SpatioTemporalTile







class EndTile(SpatioTemporalTile):
    """
    Class representing the `EndTile` entity, which inherits from:
    - SpatioTemporalTile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_edf72228_e040_4edc_8b46_78b2a47c72d7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EndTile'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EndTile(
    
    class_iri='https://w3id.org/emmo#EMMO_edf72228_e040_4edc_8b46_78b2a47c72d7',
    
    class_name='EndTile',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_edf72228_e040_4edc_8b46_78b2a47c72d7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EndTile',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    