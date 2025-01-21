
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UpAntiQuarkModule import UpAntiQuark



from .GreenAntiQuarkModule import GreenAntiQuark







class GreenUpAntiQuark(UpAntiQuark, GreenAntiQuark):
    """
    Class representing the `GreenUpAntiQuark` entity, which inherits from:
    - UpAntiQuark, GreenAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4a465306_cb91_4458_a94a_2d0584d9aa95'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenUpAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenUpAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_4a465306_cb91_4458_a94a_2d0584d9aa95',
    
    class_name='GreenUpAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4a465306_cb91_4458_a94a_2d0584d9aa95',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenUpAntiQuark',
        alias="class_name"
    )
    

    
    

    

    