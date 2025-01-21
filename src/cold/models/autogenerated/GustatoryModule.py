
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerceptualModule import Perceptual







class Gustatory(Perceptual):
    """
    Class representing the `Gustatory` entity, which inherits from:
    - Perceptual

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dd14d055_2db0_4b81_bc97_ef6c2f72b8a0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Gustatory'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Gustatory(
    
    class_iri='https://w3id.org/emmo#EMMO_dd14d055_2db0_4b81_bc97_ef6c2f72b8a0',
    
    class_name='Gustatory',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dd14d055_2db0_4b81_bc97_ef6c2f72b8a0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Gustatory',
        alias="class_name"
    )
    

    
    

    

    