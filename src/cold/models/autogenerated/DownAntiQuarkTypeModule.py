
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AntiQuarkModule import AntiQuark







class DownAntiQuarkType(AntiQuark):
    """
    Class representing the `DownAntiQuarkType` entity, which inherits from:
    - AntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a24cbaac_9595_4672_8a60_2818938cfc60'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DownAntiQuarkType'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DownAntiQuarkType(
    
    class_iri='https://w3id.org/emmo#EMMO_a24cbaac_9595_4672_8a60_2818938cfc60',
    
    class_name='DownAntiQuarkType',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a24cbaac_9595_4672_8a60_2818938cfc60',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DownAntiQuarkType',
        alias="class_name"
    )
    

    
    

    

    