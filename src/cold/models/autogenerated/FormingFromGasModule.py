
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class FormingFromGas(FromNotProperShapeToWorkPiece):
    """
    Class representing the `FormingFromGas` entity, which inherits from:
    - FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4e6c4c25_e937_40d5_9cd1_0f3b740cc0a8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormingFromGas'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormingFromGas(
    
    class_iri='https://w3id.org/emmo#EMMO_4e6c4c25_e937_40d5_9cd1_0f3b740cc0a8',
    
    class_name='FormingFromGas',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4e6c4c25_e937_40d5_9cd1_0f3b740cc0a8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormingFromGas',
        alias="class_name"
    )
    

    
    

    

    