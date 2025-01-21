
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuarkModule import Quark







class GreenQuark(Quark):
    """
    Class representing the `GreenQuark` entity, which inherits from:
    - Quark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dcc63058_f36a_4f49_a109_a8c3de88d890'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GreenQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GreenQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_dcc63058_f36a_4f49_a109_a8c3de88d890',
    
    class_name='GreenQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dcc63058_f36a_4f49_a109_a8c3de88d890',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GreenQuark',
        alias="class_name"
    )
    

    
    

    

    