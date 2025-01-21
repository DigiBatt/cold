
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BottomQuarkModule import BottomQuark



from .GreenQuarkModule import GreenQuark







class GreenBottomQuark(BottomQuark, GreenQuark):
    """
    Class representing the `GreenBottomQuark` entity, which inherits from:
    - BottomQuark, GreenQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_80252279_046c_4e33_bdf4_8932f79b6c91'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenBottomQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenBottomQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_80252279_046c_4e33_bdf4_8932f79b6c91',
    
    class_name='GreenBottomQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_80252279_046c_4e33_bdf4_8932f79b6c91',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenBottomQuark',
        alias="class_name"
    )
    

    
    

    

    