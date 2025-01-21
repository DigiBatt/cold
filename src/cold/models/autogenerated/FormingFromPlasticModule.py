
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FromNotProperShapeToWorkPieceModule import FromNotProperShapeToWorkPiece







class FormingFromPlastic(FromNotProperShapeToWorkPiece):
    """
    Class representing the `FormingFromPlastic` entity, which inherits from:
    - FromNotProperShapeToWorkPiece

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6523cad7_ea54_471c_adb7_e783f824ec09'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FormingFromPlastic'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FormingFromPlastic(
    
    class_iri='https://w3id.org/emmo#EMMO_6523cad7_ea54_471c_adb7_e783f824ec09',
    
    class_name='FormingFromPlastic',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6523cad7_ea54_471c_adb7_e783f824ec09',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FormingFromPlastic',
        alias="class_name"
    )
    

    
    

    

    