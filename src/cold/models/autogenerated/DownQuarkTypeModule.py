
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .QuarkModule import Quark







class DownQuarkType(Quark):
    """
    Class representing the `DownQuarkType` entity, which inherits from:
    - Quark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ff010476_5153_422b_99ad_0cd59b226892'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DownQuarkType'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DownQuarkType(
    
    class_iri='https://w3id.org/emmo#EMMO_ff010476_5153_422b_99ad_0cd59b226892',
    
    class_name='DownQuarkType',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ff010476_5153_422b_99ad_0cd59b226892',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DownQuarkType',
        alias="class_name"
    )
    

    
    

    

    