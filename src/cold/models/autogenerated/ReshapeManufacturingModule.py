
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkpieceManufacturingModule import WorkpieceManufacturing



from .FromWorkPIecetoWorkPieceModule import FromWorkPIecetoWorkPiece







class ReshapeManufacturing(WorkpieceManufacturing, FromWorkPIecetoWorkPiece):
    """
    Class representing the `ReshapeManufacturing` entity, which inherits from:
    - WorkpieceManufacturing, FromWorkPIecetoWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2b4783a6_36ad_48c8_8f5d_fe7c05ad298b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReshapeManufacturing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReshapeManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_2b4783a6_36ad_48c8_8f5d_fe7c05ad298b',
    
    class_name='ReshapeManufacturing',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2b4783a6_36ad_48c8_8f5d_fe7c05ad298b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReshapeManufacturing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    