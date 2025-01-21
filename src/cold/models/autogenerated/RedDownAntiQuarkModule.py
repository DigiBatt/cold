
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RedAntiQuarkModule import RedAntiQuark



from .DownAntiQuarkModule import DownAntiQuark







class RedDownAntiQuark(RedAntiQuark, DownAntiQuark):
    """
    Class representing the `RedDownAntiQuark` entity, which inherits from:
    - RedAntiQuark, DownAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b9277e83_016c_405f_b90a_7e93642c775b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedDownAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedDownAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_b9277e83_016c_405f_b90a_7e93642c775b',
    
    class_name='RedDownAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b9277e83_016c_405f_b90a_7e93642c775b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedDownAntiQuark',
        alias="class_name"
    )
    

    
    

    

    