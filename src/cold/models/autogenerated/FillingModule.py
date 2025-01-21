
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .JoinManufacturingModule import JoinManufacturing







class Filling(JoinManufacturing):
    """
    Class representing the `Filling` entity, which inherits from:
    - JoinManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_095b3c46_2b60_43cb_bade_9ee9ac969720'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Filling'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Filling(
    
    class_iri='https://w3id.org/emmo#EMMO_095b3c46_2b60_43cb_bade_9ee9ac969720',
    
    class_name='Filling',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_095b3c46_2b60_43cb_bade_9ee9ac969720',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Filling',
        alias="class_name"
    )
    

    
    

    

    