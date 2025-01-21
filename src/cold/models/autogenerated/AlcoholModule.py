
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OrganicCompoundModule import OrganicCompound







class Alcohol(OrganicCompound):
    """
    Class representing the `Alcohol` entity, which inherits from:
    - OrganicCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_961f7671_8708_4ce3_9c7d_79444adba9c0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Alcohol'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Alcohol(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_961f7671_8708_4ce3_9c7d_79444adba9c0',
    
    class_name='Alcohol',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_961f7671_8708_4ce3_9c7d_79444adba9c0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Alcohol',
        alias="class_name"
    )
    

    
    

    

    