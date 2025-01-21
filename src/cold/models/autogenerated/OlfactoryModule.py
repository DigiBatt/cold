
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerceptualModule import Perceptual







class Olfactory(Perceptual):
    """
    Class representing the `Olfactory` entity, which inherits from:
    - Perceptual

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e1021593_06da_4237_8a02_29d8f6fef76d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Olfactory'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Olfactory(
    
    class_iri='https://w3id.org/emmo#EMMO_e1021593_06da_4237_8a02_29d8f6fef76d',
    
    class_name='Olfactory',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e1021593_06da_4237_8a02_29d8f6fef76d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Olfactory',
        alias="class_name"
    )
    

    
    

    

    