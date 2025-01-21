
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .UpQuarkModule import UpQuark



from .GreenQuarkModule import GreenQuark







class GreenUpQuark(UpQuark, GreenQuark):
    """
    Class representing the `GreenUpQuark` entity, which inherits from:
    - UpQuark, GreenQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b57afc1a_93e9_43ba_b41f_9ec3598b4e46'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenUpQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenUpQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_b57afc1a_93e9_43ba_b41f_9ec3598b4e46',
    
    class_name='GreenUpQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b57afc1a_93e9_43ba_b41f_9ec3598b4e46',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenUpQuark',
        alias="class_name"
    )
    

    
    

    

    