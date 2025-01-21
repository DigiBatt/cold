
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GluonModule import Gluon







class GluonType7(Gluon):
    """
    Class representing the `GluonType7` entity, which inherits from:
    - Gluon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9668ae43_d1a0_43ae_a91a_9051512b0a54'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GluonType7'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GluonType7(
    
    class_iri='https://w3id.org/emmo#EMMO_9668ae43_d1a0_43ae_a91a_9051512b0a54',
    
    class_name='GluonType7',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9668ae43_d1a0_43ae_a91a_9051512b0a54',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GluonType7',
        alias="class_name"
    )
    

    
    

    

    