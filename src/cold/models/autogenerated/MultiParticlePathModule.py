
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalPathModule import CausalPath







class MultiParticlePath(CausalPath):
    """
    Class representing the `MultiParticlePath` entity, which inherits from:
    - CausalPath

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5e00b1db_48fc_445b_82e8_ab0e2255bf52'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MultiParticlePath'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MultiParticlePath(
    
    class_iri='https://w3id.org/emmo#EMMO_5e00b1db_48fc_445b_82e8_ab0e2255bf52',
    
    class_name='MultiParticlePath',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5e00b1db_48fc_445b_82e8_ab0e2255bf52',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MultiParticlePath',
        alias="class_name"
    )
    

    
    

    

    