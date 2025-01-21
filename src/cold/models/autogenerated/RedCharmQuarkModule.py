
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharmQuarkModule import CharmQuark



from .RedQuarkModule import RedQuark







class RedCharmQuark(CharmQuark, RedQuark):
    """
    Class representing the `RedCharmQuark` entity, which inherits from:
    - CharmQuark, RedQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_225775f9_3bf3_4309_a7e1_aa7305c9278a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedCharmQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedCharmQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_225775f9_3bf3_4309_a7e1_aa7305c9278a',
    
    class_name='RedCharmQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_225775f9_3bf3_4309_a7e1_aa7305c9278a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedCharmQuark',
        alias="class_name"
    )
    

    
    

    

    