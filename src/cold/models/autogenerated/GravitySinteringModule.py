
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SinteringModule import Sintering







class GravitySintering(Sintering):
    """
    Class representing the `GravitySintering` entity, which inherits from:
    - Sintering

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3ec45f3b_677d_4e71_be75_6f8966b4f808'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GravitySintering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = GravitySintering(
    
    class_iri='https://w3id.org/emmo#EMMO_3ec45f3b_677d_4e71_be75_6f8966b4f808',
    
    class_name='GravitySintering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3ec45f3b_677d_4e71_be75_6f8966b4f808',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GravitySintering',
        alias="class_name"
    )
    

    
    

    

    