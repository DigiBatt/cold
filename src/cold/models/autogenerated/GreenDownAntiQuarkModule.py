
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DownAntiQuarkModule import DownAntiQuark



from .GreenAntiQuarkModule import GreenAntiQuark







class GreenDownAntiQuark(DownAntiQuark, GreenAntiQuark):
    """
    Class representing the `GreenDownAntiQuark` entity, which inherits from:
    - DownAntiQuark, GreenAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ab5ba485_7c16_4c9e_b65e_4cb7560f8e8c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenDownAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenDownAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_ab5ba485_7c16_4c9e_b65e_4cb7560f8e8c',
    
    class_name='GreenDownAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ab5ba485_7c16_4c9e_b65e_4cb7560f8e8c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenDownAntiQuark',
        alias="class_name"
    )
    

    
    

    

    