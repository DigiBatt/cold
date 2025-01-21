
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .JoinManufacturingModule import JoinManufacturing







class Gluing(JoinManufacturing):
    """
    Class representing the `Gluing` entity, which inherits from:
    - JoinManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ecc10f05_b301_4dcf_8c84_b6f511117234'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Gluing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Gluing(
    
    class_iri='https://w3id.org/emmo#EMMO_ecc10f05_b301_4dcf_8c84_b6f511117234',
    
    class_name='Gluing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ecc10f05_b301_4dcf_8c84_b6f511117234',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Gluing',
        alias="class_name"
    )
    

    
    

    

    