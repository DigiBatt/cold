
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UpQuarkModule import UpQuark



from .RedQuarkModule import RedQuark







class RedUpQuark(UpQuark, RedQuark):
    """
    Class representing the `RedUpQuark` entity, which inherits from:
    - UpQuark, RedQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_506cb971_797d_4cfb_88c3_3020c4396365'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedUpQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedUpQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_506cb971_797d_4cfb_88c3_3020c4396365',
    
    class_name='RedUpQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_506cb971_797d_4cfb_88c3_3020c4396365',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedUpQuark',
        alias="class_name"
    )
    

    
    

    

    