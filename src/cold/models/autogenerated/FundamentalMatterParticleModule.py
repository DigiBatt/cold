
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalFermionModule import FundamentalFermion







class FundamentalMatterParticle(FundamentalFermion):
    """
    Class representing the `FundamentalMatterParticle` entity, which inherits from:
    - FundamentalFermion

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_dad35c10_dd6c_4602_8474_f4ef68517fe9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FundamentalMatterParticle'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FundamentalMatterParticle(
    
    class_iri='https://w3id.org/emmo#EMMO_dad35c10_dd6c_4602_8474_f4ef68517fe9',
    
    class_name='FundamentalMatterParticle',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_dad35c10_dd6c_4602_8474_f4ef68517fe9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FundamentalMatterParticle',
        alias="class_name"
    )
    

    
    

    

    