
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BottomAntiQuarkModule import BottomAntiQuark



from .GreenAntiQuarkModule import GreenAntiQuark







class GreenBottomAntiQuark(BottomAntiQuark, GreenAntiQuark):
    """
    Class representing the `GreenBottomAntiQuark` entity, which inherits from:
    - BottomAntiQuark, GreenAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_88ca735d_af0e_4773_b769_9c9bc6f8f91c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenBottomAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenBottomAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_88ca735d_af0e_4773_b769_9c9bc6f8f91c',
    
    class_name='GreenBottomAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_88ca735d_af0e_4773_b769_9c9bc6f8f91c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenBottomAntiQuark',
        alias="class_name"
    )
    

    
    

    

    