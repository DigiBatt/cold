
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DownQuarkModule import DownQuark



from .RedQuarkModule import RedQuark







class RedDownQuark(DownQuark, RedQuark):
    """
    Class representing the `RedDownQuark` entity, which inherits from:
    - DownQuark, RedQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d16ce022_5298_49a3_87a5_ca883faae18c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedDownQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedDownQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_d16ce022_5298_49a3_87a5_ca883faae18c',
    
    class_name='RedDownQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d16ce022_5298_49a3_87a5_ca883faae18c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedDownQuark',
        alias="class_name"
    )
    

    
    

    

    