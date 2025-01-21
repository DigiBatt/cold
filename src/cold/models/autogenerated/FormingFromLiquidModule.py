
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class FormingFromLiquid(FromNotProperShapeToWorkPiece):
    """
    Class representing the `FormingFromLiquid` entity, which inherits from:
    - FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d7432d8c_3182_4d61_a08f_dc686efaabe9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormingFromLiquid'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormingFromLiquid(
    
    class_iri='https://w3id.org/emmo#EMMO_d7432d8c_3182_4d61_a08f_dc686efaabe9',
    
    class_name='FormingFromLiquid',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d7432d8c_3182_4d61_a08f_dc686efaabe9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormingFromLiquid',
        alias="class_name"
    )
    

    
    

    

    