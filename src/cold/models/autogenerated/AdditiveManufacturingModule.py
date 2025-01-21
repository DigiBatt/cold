
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class AdditiveManufacturing(FromNotProperShapeToWorkPiece):
    """
    Class representing the `AdditiveManufacturing` entity, which inherits from:
    - FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_03eb9b46_8ff0_4fcd_b1a0_73f65ae7434e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AdditiveManufacturing'`
        - **Alias**: `class_name`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AdditiveManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_03eb9b46_8ff0_4fcd_b1a0_73f65ae7434e',
    
    class_name='AdditiveManufacturing',
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_03eb9b46_8ff0_4fcd_b1a0_73f65ae7434e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AdditiveManufacturing',
        alias="class_name"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    