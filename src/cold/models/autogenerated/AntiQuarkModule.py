
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalAntiMatterParticleModule import FundamentalAntiMatterParticle







class AntiQuark(FundamentalAntiMatterParticle):
    """
    Class representing the `AntiQuark` entity, which inherits from:
    - FundamentalAntiMatterParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cc741dde_2c7c_46ef_bb66_16a6d12c2a88'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_cc741dde_2c7c_46ef_bb66_16a6d12c2a88',
    
    class_name='AntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cc741dde_2c7c_46ef_bb66_16a6d12c2a88',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AntiQuark',
        alias="class_name"
    )
    

    
    

    

    