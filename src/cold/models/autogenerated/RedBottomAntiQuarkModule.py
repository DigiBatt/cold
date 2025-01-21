
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BottomAntiQuarkModule import BottomAntiQuark



from .RedAntiQuarkModule import RedAntiQuark







class RedBottomAntiQuark(BottomAntiQuark, RedAntiQuark):
    """
    Class representing the `RedBottomAntiQuark` entity, which inherits from:
    - BottomAntiQuark, RedAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1f8f92a8_4cc9_4fa3_9b5f_d5af5bab4fd2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedBottomAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedBottomAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_1f8f92a8_4cc9_4fa3_9b5f_d5af5bab4fd2',
    
    class_name='RedBottomAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1f8f92a8_4cc9_4fa3_9b5f_d5af5bab4fd2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedBottomAntiQuark',
        alias="class_name"
    )
    

    
    

    

    