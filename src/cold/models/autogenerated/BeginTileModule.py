
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpatioTemporalTileModule import SpatioTemporalTile







class BeginTile(SpatioTemporalTile):
    """
    Class representing the `BeginTile` entity, which inherits from:
    - SpatioTemporalTile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fa595892_070d_455e_9459_06c97179c080'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BeginTile'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BeginTile(
    
    class_iri='https://w3id.org/emmo#EMMO_fa595892_070d_455e_9459_06c97179c080',
    
    class_name='BeginTile',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fa595892_070d_455e_9459_06c97179c080',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BeginTile',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    