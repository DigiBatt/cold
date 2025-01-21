
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BlueAntiQuarkModule import BlueAntiQuark



from .DownAntiQuarkModule import DownAntiQuark







class BlueDownAntiQuark(BlueAntiQuark, DownAntiQuark):
    """
    Class representing the `BlueDownAntiQuark` entity, which inherits from:
    - BlueAntiQuark, DownAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9d6eeca7_89a0_4a65_a497_9039f1164b96'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueDownAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueDownAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_9d6eeca7_89a0_4a65_a497_9039f1164b96',
    
    class_name='BlueDownAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9d6eeca7_89a0_4a65_a497_9039f1164b96',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueDownAntiQuark',
        alias="class_name"
    )
    

    
    

    

    