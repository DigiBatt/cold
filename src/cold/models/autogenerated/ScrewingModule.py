
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PressingModule import Pressing







class Screwing(Pressing):
    """
    Class representing the `Screwing` entity, which inherits from:
    - Pressing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_410b5956_a06d_4370_b7df_b1bd2126fb4b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Screwing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Screwing(
    
    class_iri='https://w3id.org/emmo#EMMO_410b5956_a06d_4370_b7df_b1bd2126fb4b',
    
    class_name='Screwing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_410b5956_a06d_4370_b7df_b1bd2126fb4b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Screwing',
        alias="class_name"
    )
    

    
    

    

    