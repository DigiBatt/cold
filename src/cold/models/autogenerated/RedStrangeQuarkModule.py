
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrangeQuarkModule import StrangeQuark



from .RedQuarkModule import RedQuark







class RedStrangeQuark(StrangeQuark, RedQuark):
    """
    Class representing the `RedStrangeQuark` entity, which inherits from:
    - StrangeQuark, RedQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9eb96ea0_8827_4cb9_9a03_8e07f4eae1eb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedStrangeQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedStrangeQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_9eb96ea0_8827_4cb9_9a03_8e07f4eae1eb',
    
    class_name='RedStrangeQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9eb96ea0_8827_4cb9_9a03_8e07f4eae1eb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedStrangeQuark',
        alias="class_name"
    )
    

    
    

    

    