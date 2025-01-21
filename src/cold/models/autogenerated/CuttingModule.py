
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparateManufacturingModule import SeparateManufacturing







class Cutting(SeparateManufacturing):
    """
    Class representing the `Cutting` entity, which inherits from:
    - SeparateManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d5f98475_00ce_4987_99fb_262aed395e46'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Cutting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Cutting(
    
    class_iri='https://w3id.org/emmo#EMMO_d5f98475_00ce_4987_99fb_262aed395e46',
    
    class_name='Cutting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d5f98475_00ce_4987_99fb_262aed395e46',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Cutting',
        alias="class_name"
    )
    

    
    

    

    