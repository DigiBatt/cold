
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .JoinManufacturingModule import JoinManufacturing







class Soldering(JoinManufacturing):
    """
    Class representing the `Soldering` entity, which inherits from:
    - JoinManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c790c7ff_2d10_4336_94ad_4f4e173109a9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Soldering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Soldering(
    
    class_iri='https://w3id.org/emmo#EMMO_c790c7ff_2d10_4336_94ad_4f4e173109a9',
    
    class_name='Soldering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c790c7ff_2d10_4336_94ad_4f4e173109a9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Soldering',
        alias="class_name"
    )
    

    
    

    

    