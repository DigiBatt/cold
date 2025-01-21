
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalFermionModule import FundamentalFermion







class FundamentalAntiMatterParticle(FundamentalFermion):
    """
    Class representing the `FundamentalAntiMatterParticle` entity, which inherits from:
    - FundamentalFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9226c7af_573f_4762_865c_e3a68a4832dd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FundamentalAntiMatterParticle'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FundamentalAntiMatterParticle(
    
    class_iri='https://w3id.org/emmo#EMMO_9226c7af_573f_4762_865c_e3a68a4832dd',
    
    class_name='FundamentalAntiMatterParticle',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9226c7af_573f_4762_865c_e3a68a4832dd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FundamentalAntiMatterParticle',
        alias="class_name"
    )
    

    
    

    

    