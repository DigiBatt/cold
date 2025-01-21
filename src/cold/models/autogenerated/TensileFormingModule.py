
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReshapeManufacturingModule import ReshapeManufacturing







class TensileForming(ReshapeManufacturing):
    """
    Class representing the `TensileForming` entity, which inherits from:
    - ReshapeManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6fba4018_24bd_450c_abc3_354e2c7809c9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TensileForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TensileForming(
    
    class_iri='https://w3id.org/emmo#EMMO_6fba4018_24bd_450c_abc3_354e2c7809c9',
    
    class_name='TensileForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6fba4018_24bd_450c_abc3_354e2c7809c9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TensileForming',
        alias="class_name"
    )
    

    
    

    

    