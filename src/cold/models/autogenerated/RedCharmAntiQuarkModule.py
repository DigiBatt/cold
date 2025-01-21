
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharmAntiQuarkModule import CharmAntiQuark



from .RedAntiQuarkModule import RedAntiQuark







class RedCharmAntiQuark(CharmAntiQuark, RedAntiQuark):
    """
    Class representing the `RedCharmAntiQuark` entity, which inherits from:
    - CharmAntiQuark, RedAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_aeebc6d5_bf98_45c1_b3eb_89de6722ba46'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedCharmAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedCharmAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_aeebc6d5_bf98_45c1_b3eb_89de6722ba46',
    
    class_name='RedCharmAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_aeebc6d5_bf98_45c1_b3eb_89de6722ba46',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedCharmAntiQuark',
        alias="class_name"
    )
    

    
    

    

    