
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReshapeManufacturingModule import ReshapeManufacturing







class ShearForming(ReshapeManufacturing):
    """
    Class representing the `ShearForming` entity, which inherits from:
    - ReshapeManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_22744495_4f32_4a17_b189_259c644268f9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ShearForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ShearForming(
    
    class_iri='https://w3id.org/emmo#EMMO_22744495_4f32_4a17_b189_259c644268f9',
    
    class_name='ShearForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_22744495_4f32_4a17_b189_259c644268f9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ShearForming',
        alias="class_name"
    )
    

    
    

    

    