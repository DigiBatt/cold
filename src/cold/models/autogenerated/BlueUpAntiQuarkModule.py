
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UpAntiQuarkModule import UpAntiQuark



from .BlueAntiQuarkModule import BlueAntiQuark







class BlueUpAntiQuark(UpAntiQuark, BlueAntiQuark):
    """
    Class representing the `BlueUpAntiQuark` entity, which inherits from:
    - UpAntiQuark, BlueAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4cc06415_9c11_4071_b732_fd05ad750f07'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueUpAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueUpAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_4cc06415_9c11_4071_b732_fd05ad750f07',
    
    class_name='BlueUpAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4cc06415_9c11_4071_b732_fd05ad750f07',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueUpAntiQuark',
        alias="class_name"
    )
    

    
    

    

    