
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class FormingFromPulp(FromNotProperShapeToWorkPiece):
    """
    Class representing the `FormingFromPulp` entity, which inherits from:
    - FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a46f2e3f_6d06_4968_a02f_55274d131130'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormingFromPulp'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormingFromPulp(
    
    class_iri='https://w3id.org/emmo#EMMO_a46f2e3f_6d06_4968_a02f_55274d131130',
    
    class_name='FormingFromPulp',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a46f2e3f_6d06_4968_a02f_55274d131130',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormingFromPulp',
        alias="class_name"
    )
    

    
    

    

    