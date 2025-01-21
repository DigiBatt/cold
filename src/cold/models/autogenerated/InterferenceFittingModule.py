
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PressingModule import Pressing







class InterferenceFitting(Pressing):
    """
    Class representing the `InterferenceFitting` entity, which inherits from:
    - Pressing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_26f34447_32ec_48ce_9baa_4afec09120f4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InterferenceFitting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InterferenceFitting(
    
    class_iri='https://w3id.org/emmo#EMMO_26f34447_32ec_48ce_9baa_4afec09120f4',
    
    class_name='InterferenceFitting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_26f34447_32ec_48ce_9baa_4afec09120f4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InterferenceFitting',
        alias="class_name"
    )
    

    
    

    

    