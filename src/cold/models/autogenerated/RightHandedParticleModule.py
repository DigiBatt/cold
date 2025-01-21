
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalFermionModule import FundamentalFermion







class RightHandedParticle(FundamentalFermion):
    """
    Class representing the `RightHandedParticle` entity, which inherits from:
    - FundamentalFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_07bb613c_e8d0_425f_abcc_47c58b14704e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RightHandedParticle'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RightHandedParticle(
    
    class_iri='https://w3id.org/emmo#EMMO_07bb613c_e8d0_425f_abcc_47c58b14704e',
    
    class_name='RightHandedParticle',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_07bb613c_e8d0_425f_abcc_47c58b14704e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RightHandedParticle',
        alias="class_name"
    )
    

    
    

    

    