
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompressiveFormingModule import CompressiveForming



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class Moulding(CompressiveForming, FromNotProperShapeToWorkPiece):
    """
    Class representing the `Moulding` entity, which inherits from:
    - CompressiveForming, FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6800c3fd_bf5d_4a2a_8e6e_9e909eefc16c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Moulding'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Moulding(
    
    class_iri='https://w3id.org/emmo#EMMO_6800c3fd_bf5d_4a2a_8e6e_9e909eefc16c',
    
    class_name='Moulding',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6800c3fd_bf5d_4a2a_8e6e_9e909eefc16c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Moulding',
        alias="class_name"
    )
    

    
    

    

    