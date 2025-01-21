
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReshapeManufacturingModule import ReshapeManufacturing







class CompressiveForming(ReshapeManufacturing):
    """
    Class representing the `CompressiveForming` entity, which inherits from:
    - ReshapeManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_39d5c9c4_7d24_4409_ba3b_60ca3afde902'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CompressiveForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CompressiveForming(
    
    class_iri='https://w3id.org/emmo#EMMO_39d5c9c4_7d24_4409_ba3b_60ca3afde902',
    
    class_name='CompressiveForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_39d5c9c4_7d24_4409_ba3b_60ca3afde902',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CompressiveForming',
        alias="class_name"
    )
    

    
    

    

    