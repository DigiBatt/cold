
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WetCellModule import WetCell







class LeclancheWetCell(WetCell):
    """
    Class representing the `LeclancheWetCell` entity, which inherits from:
    - WetCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_8c391d2a_7d44_49a2_affd_176afd3d4ba4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LeclancheWetCell'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LeclancheWetCell(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_8c391d2a_7d44_49a2_affd_176afd3d4ba4',
    
    class_name='LeclancheWetCell',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_8c391d2a_7d44_49a2_affd_176afd3d4ba4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LeclancheWetCell',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    