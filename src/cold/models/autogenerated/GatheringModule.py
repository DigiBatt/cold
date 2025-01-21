
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MixedTilingModule import MixedTiling







class Gathering(MixedTiling):
    """
    Class representing the `Gathering` entity, which inherits from:
    - MixedTiling

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b1862e72_219f_4fc0_b58c_b26339f6dc88'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Gathering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Gathering(
    
    class_iri='https://w3id.org/emmo#EMMO_b1862e72_219f_4fc0_b58c_b26339f6dc88',
    
    class_name='Gathering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b1862e72_219f_4fc0_b58c_b26339f6dc88',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Gathering',
        alias="class_name"
    )
    

    
    

    

    