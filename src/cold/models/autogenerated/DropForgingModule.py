
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReshapeManufacturingModule import ReshapeManufacturing







class DropForging(ReshapeManufacturing):
    """
    Class representing the `DropForging` entity, which inherits from:
    - ReshapeManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4e099d7e_f624_4761_aff6_2ee6c63b8d2d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DropForging'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DropForging(
    
    class_iri='https://w3id.org/emmo#EMMO_4e099d7e_f624_4761_aff6_2ee6c63b8d2d',
    
    class_name='DropForging',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4e099d7e_f624_4761_aff6_2ee6c63b8d2d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DropForging',
        alias="class_name"
    )
    

    
    

    

    