
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .JoinManufacturingModule import JoinManufacturing







class Welding(JoinManufacturing):
    """
    Class representing the `Welding` entity, which inherits from:
    - JoinManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_06c415dc_ba26_407d_b596_283bd4d9a66f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Welding'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Welding(
    
    class_iri='https://w3id.org/emmo#EMMO_06c415dc_ba26_407d_b596_283bd4d9a66f',
    
    class_name='Welding',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_06c415dc_ba26_407d_b596_283bd4d9a66f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Welding',
        alias="class_name"
    )
    

    
    

    

    