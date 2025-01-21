
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeviceModule import Device







class TransportationDevice(Device):
    """
    Class representing the `TransportationDevice` entity, which inherits from:
    - Device

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_95d4eb9b_d3d0_4705_a01c_4f87fb5f8d43'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransportationDevice'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TransportationDevice(
    
    class_iri='https://w3id.org/emmo#EMMO_95d4eb9b_d3d0_4705_a01c_4f87fb5f8d43',
    
    class_name='TransportationDevice',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_95d4eb9b_d3d0_4705_a01c_4f87fb5f8d43',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransportationDevice',
        alias="class_name"
    )
    

    
    

    

    