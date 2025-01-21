
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeviceModule import Device







class InspectionDevice(Device):
    """
    Class representing the `InspectionDevice` entity, which inherits from:
    - Device

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3967de47_343f_4bab_aada_b4bec73d11da'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InspectionDevice'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InspectionDevice(
    
    class_iri='https://w3id.org/emmo#EMMO_3967de47_343f_4bab_aada_b4bec73d11da',
    
    class_name='InspectionDevice',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3967de47_343f_4bab_aada_b4bec73d11da',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InspectionDevice',
        alias="class_name"
    )
    

    
    

    

    