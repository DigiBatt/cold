
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReshapeManufacturingModule import ReshapeManufacturing







class FlexuralForming(ReshapeManufacturing):
    """
    Class representing the `FlexuralForming` entity, which inherits from:
    - ReshapeManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_aced32dd_1a13_49b0_8d8f_c79313942d19'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FlexuralForming'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FlexuralForming(
    
    class_iri='https://w3id.org/emmo#EMMO_aced32dd_1a13_49b0_8d8f_c79313942d19',
    
    class_name='FlexuralForming',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_aced32dd_1a13_49b0_8d8f_c79313942d19',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FlexuralForming',
        alias="class_name"
    )
    

    
    

    

    