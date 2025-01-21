
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class MicrowaveSintering(Sintering):
    """
    Class representing the `MicrowaveSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0342678c_13ba_43d7_9cbd_df60967a0a45'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MicrowaveSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MicrowaveSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_0342678c_13ba_43d7_9cbd_df60967a0a45',
    
    class_name='MicrowaveSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0342678c_13ba_43d7_9cbd_df60967a0a45',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MicrowaveSintering',
        alias="class_name"
    )
    

    
    

    

    