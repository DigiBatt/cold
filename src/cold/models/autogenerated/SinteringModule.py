
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class Sintering(FromNotProperShapeToWorkPiece):
    """
    Class representing the `Sintering` entity, which inherits from:
    - FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_03441eb3_d1fd_4906_b953_b83312d7589e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Sintering'`
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
    obj = Sintering(
    
    class_iri='https://w3id.org/emmo#EMMO_03441eb3_d1fd_4906_b953_b83312d7589e',
    
    class_name='Sintering',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_03441eb3_d1fd_4906_b953_b83312d7589e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Sintering',
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
    

    
    

    

    