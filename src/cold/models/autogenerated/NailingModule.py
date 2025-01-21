
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PressingModule import Pressing







class Nailing(Pressing):
    """
    Class representing the `Nailing` entity, which inherits from:
    - Pressing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4f46c5ab_1c21_4639_90d5_3c4ebf3b156b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Nailing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Nailing(
    
    class_iri='https://w3id.org/emmo#EMMO_4f46c5ab_1c21_4639_90d5_3c4ebf3b156b',
    
    class_name='Nailing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4f46c5ab_1c21_4639_90d5_3c4ebf3b156b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Nailing',
        alias="class_name"
    )
    

    
    

    

    