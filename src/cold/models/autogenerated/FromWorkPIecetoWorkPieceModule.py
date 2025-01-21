
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkpieceFormingModule import WorkpieceForming







class FromWorkPIecetoWorkPiece(WorkpieceForming):
    """
    Class representing the `FromWorkPIecetoWorkPiece` entity, which inherits from:
    - WorkpieceForming

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fc86c700_ccea_441c_b628_ad236f030fe6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FromWorkPIecetoWorkPiece'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FromWorkPIecetoWorkPiece(
    
    class_iri='https://w3id.org/emmo#EMMO_fc86c700_ccea_441c_b628_ad236f030fe6',
    
    class_name='FromWorkPIecetoWorkPiece',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fc86c700_ccea_441c_b628_ad236f030fe6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FromWorkPIecetoWorkPiece',
        alias="class_name"
    )
    

    
    

    

    