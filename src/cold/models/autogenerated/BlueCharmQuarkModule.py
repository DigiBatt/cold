
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharmQuarkModule import CharmQuark



from .BlueQuarkModule import BlueQuark







class BlueCharmQuark(CharmQuark, BlueQuark):
    """
    Class representing the `BlueCharmQuark` entity, which inherits from:
    - CharmQuark, BlueQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1d2bf964_5d54_4da6_a02d_7c908517ef91'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BlueCharmQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BlueCharmQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_1d2bf964_5d54_4da6_a02d_7c908517ef91',
    
    class_name='BlueCharmQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1d2bf964_5d54_4da6_a02d_7c908517ef91',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BlueCharmQuark',
        alias="class_name"
    )
    

    
    

    

    