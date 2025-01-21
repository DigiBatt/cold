
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AntiQuarkModule import AntiQuark







class RedAntiQuark(AntiQuark):
    """
    Class representing the `RedAntiQuark` entity, which inherits from:
    - AntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_74fd4dfc_a59e_4f66_8822_7fc3ad8a0664'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_74fd4dfc_a59e_4f66_8822_7fc3ad8a0664',
    
    class_name='RedAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_74fd4dfc_a59e_4f66_8822_7fc3ad8a0664',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedAntiQuark',
        alias="class_name"
    )
    

    
    

    

    