
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharmAntiQuarkModule import CharmAntiQuark



from .BlueAntiQuarkModule import BlueAntiQuark







class BlueCharmAntiQuark(CharmAntiQuark, BlueAntiQuark):
    """
    Class representing the `BlueCharmAntiQuark` entity, which inherits from:
    - CharmAntiQuark, BlueAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5a77b7a6_7b16_48cd_8d69_a0c4b9174a3f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueCharmAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueCharmAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_5a77b7a6_7b16_48cd_8d69_a0c4b9174a3f',
    
    class_name='BlueCharmAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5a77b7a6_7b16_48cd_8d69_a0c4b9174a3f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueCharmAntiQuark',
        alias="class_name"
    )
    

    
    

    

    