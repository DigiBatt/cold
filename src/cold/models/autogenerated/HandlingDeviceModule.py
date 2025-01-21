
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeviceModule import Device







class HandlingDevice(Device):
    """
    Class representing the `HandlingDevice` entity, which inherits from:
    - Device

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2565210a_bbcc_4c00_a122_6a608faa355b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HandlingDevice'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HandlingDevice(
    
    class_iri='https://w3id.org/emmo#EMMO_2565210a_bbcc_4c00_a122_6a608faa355b',
    
    class_name='HandlingDevice',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2565210a_bbcc_4c00_a122_6a608faa355b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HandlingDevice',
        alias="class_name"
    )
    

    
    

    

    