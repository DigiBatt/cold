
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RedQuarkModule import RedQuark



from .BottomQuarkModule import BottomQuark







class RedBottomQuark(RedQuark, BottomQuark):
    """
    Class representing the `RedBottomQuark` entity, which inherits from:
    - RedQuark, BottomQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_387b0334_aff8_4b3f_9062_8ad051f72e91'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedBottomQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedBottomQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_387b0334_aff8_4b3f_9062_8ad051f72e91',
    
    class_name='RedBottomQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_387b0334_aff8_4b3f_9062_8ad051f72e91',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedBottomQuark',
        alias="class_name"
    )
    

    
    

    

    