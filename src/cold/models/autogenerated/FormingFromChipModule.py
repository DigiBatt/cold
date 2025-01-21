
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class FormingFromChip(FromNotProperShapeToWorkPiece):
    """
    Class representing the `FormingFromChip` entity, which inherits from:
    - FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5e5656ef_971e_49e6_a32f_048b6e86c3e0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormingFromChip'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormingFromChip(
    
    class_iri='https://w3id.org/emmo#EMMO_5e5656ef_971e_49e6_a32f_048b6e86c3e0',
    
    class_name='FormingFromChip',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5e5656ef_971e_49e6_a32f_048b6e86c3e0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormingFromChip',
        alias="class_name"
    )
    

    
    

    

    