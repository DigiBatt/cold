
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatingManufacturingModule import CoatingManufacturing







class Painting(CoatingManufacturing):
    """
    Class representing the `Painting` entity, which inherits from:
    - CoatingManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_96c38f8d_fabd_41dc_abda_d15419eb897d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Painting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Painting(
    
    class_iri='https://w3id.org/emmo#EMMO_96c38f8d_fabd_41dc_abda_d15419eb897d',
    
    class_name='Painting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_96c38f8d_fabd_41dc_abda_d15419eb897d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Painting',
        alias="class_name"
    )
    

    
    

    

    