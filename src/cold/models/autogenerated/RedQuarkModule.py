
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuarkModule import Quark







class RedQuark(Quark):
    """
    Class representing the `RedQuark` entity, which inherits from:
    - Quark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cf972459_e649_4aa8_9676_3d219b5e0fe6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_cf972459_e649_4aa8_9676_3d219b5e0fe6',
    
    class_name='RedQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cf972459_e649_4aa8_9676_3d219b5e0fe6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedQuark',
        alias="class_name"
    )
    

    
    

    

    