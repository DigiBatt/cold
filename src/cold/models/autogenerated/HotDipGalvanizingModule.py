
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoatingManufacturingModule import CoatingManufacturing







class HotDipGalvanizing(CoatingManufacturing):
    """
    Class representing the `HotDipGalvanizing` entity, which inherits from:
    - CoatingManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_47eea65c_e6ce_4c95_9406_fdb1519abc87'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HotDipGalvanizing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HotDipGalvanizing(
    
    class_iri='https://w3id.org/emmo#EMMO_47eea65c_e6ce_4c95_9406_fdb1519abc87',
    
    class_name='HotDipGalvanizing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_47eea65c_e6ce_4c95_9406_fdb1519abc87',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HotDipGalvanizing',
        alias="class_name"
    )
    

    
    

    

    