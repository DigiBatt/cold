
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalFermionModule import FundamentalFermion







class LeftHandedParticle(FundamentalFermion):
    """
    Class representing the `LeftHandedParticle` entity, which inherits from:
    - FundamentalFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8ab3ff9d_35d4_44b7_9d66_7b0b30c40da8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LeftHandedParticle'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LeftHandedParticle(
    
    class_iri='https://w3id.org/emmo#EMMO_8ab3ff9d_35d4_44b7_9d66_7b0b30c40da8',
    
    class_name='LeftHandedParticle',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8ab3ff9d_35d4_44b7_9d66_7b0b30c40da8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LeftHandedParticle',
        alias="class_name"
    )
    

    
    

    

    