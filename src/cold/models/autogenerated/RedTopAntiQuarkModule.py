
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RedAntiQuarkModule import RedAntiQuark



from .TopAntiQuarkModule import TopAntiQuark







class RedTopAntiQuark(RedAntiQuark, TopAntiQuark):
    """
    Class representing the `RedTopAntiQuark` entity, which inherits from:
    - RedAntiQuark, TopAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9bb271f2_80a1_481a_ba78_368c4dccc235'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedTopAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedTopAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_9bb271f2_80a1_481a_ba78_368c4dccc235',
    
    class_name='RedTopAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9bb271f2_80a1_481a_ba78_368c4dccc235',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedTopAntiQuark',
        alias="class_name"
    )
    

    
    

    

    