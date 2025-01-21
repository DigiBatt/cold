
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class ReactionSintering(Sintering):
    """
    Class representing the `ReactionSintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2b524942_4e3e_403a_b4ab_2b53750f3d3b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReactionSintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReactionSintering(
    
    class_iri='https://w3id.org/emmo#EMMO_2b524942_4e3e_403a_b4ab_2b53750f3d3b',
    
    class_name='ReactionSintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2b524942_4e3e_403a_b4ab_2b53750f3d3b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReactionSintering',
        alias="class_name"
    )
    

    
    

    

    