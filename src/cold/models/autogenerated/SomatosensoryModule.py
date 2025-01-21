
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerceptualModule import Perceptual







class Somatosensory(Perceptual):
    """
    Class representing the `Somatosensory` entity, which inherits from:
    - Perceptual

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8f207971_aaab_48dc_a10d_55a6b4331410'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Somatosensory'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Somatosensory(
    
    class_iri='https://w3id.org/emmo#EMMO_8f207971_aaab_48dc_a10d_55a6b4331410',
    
    class_name='Somatosensory',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8f207971_aaab_48dc_a10d_55a6b4331410',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Somatosensory',
        alias="class_name"
    )
    

    
    

    

    