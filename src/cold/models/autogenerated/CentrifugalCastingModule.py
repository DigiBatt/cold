
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CastingModule import Casting







class CentrifugalCasting(Casting):
    """
    Class representing the `CentrifugalCasting` entity, which inherits from:
    - Casting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e1f38566_ba25_4c09_9282_eea2b86cb90b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CentrifugalCasting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CentrifugalCasting(
    
    class_iri='https://w3id.org/emmo#EMMO_e1f38566_ba25_4c09_9282_eea2b86cb90b',
    
    class_name='CentrifugalCasting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e1f38566_ba25_4c09_9282_eea2b86cb90b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CentrifugalCasting',
        alias="class_name"
    )
    

    
    

    

    