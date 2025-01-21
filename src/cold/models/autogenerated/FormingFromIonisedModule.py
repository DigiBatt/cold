
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class FormingFromIonised(FromNotProperShapeToWorkPiece):
    """
    Class representing the `FormingFromIonised` entity, which inherits from:
    - FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_326e7731_76c5_402d_a041_c9b48a736963'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormingFromIonised'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormingFromIonised(
    
    class_iri='https://w3id.org/emmo#EMMO_326e7731_76c5_402d_a041_c9b48a736963',
    
    class_name='FormingFromIonised',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_326e7731_76c5_402d_a041_c9b48a736963',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormingFromIonised',
        alias="class_name"
    )
    

    
    

    

    