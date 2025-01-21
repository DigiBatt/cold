
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AntiQuarkModule import AntiQuark







class BlueAntiQuark(AntiQuark):
    """
    Class representing the `BlueAntiQuark` entity, which inherits from:
    - AntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c88a0f70_482b_4e37_9ae2_ee66bbfc20a7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_c88a0f70_482b_4e37_9ae2_ee66bbfc20a7',
    
    class_name='BlueAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c88a0f70_482b_4e37_9ae2_ee66bbfc20a7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueAntiQuark',
        alias="class_name"
    )
    

    
    

    

    