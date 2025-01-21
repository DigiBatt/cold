
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class CeramicSintering(Sintering):
    """
    Class representing the `CeramicSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c0ec56d1_0deb_4452_a6a1_70570308b6bb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CeramicSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CeramicSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_c0ec56d1_0deb_4452_a6a1_70570308b6bb',
    
    class_name='CeramicSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c0ec56d1_0deb_4452_a6a1_70570308b6bb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CeramicSintering',
        alias="class_name"
    )
    

    
    

    

    