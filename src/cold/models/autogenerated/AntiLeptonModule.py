
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalAntiMatterParticleModule import FundamentalAntiMatterParticle







class AntiLepton(FundamentalAntiMatterParticle):
    """
    Class representing the `AntiLepton` entity, which inherits from:
    - FundamentalAntiMatterParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_716fadba_7ff8_4247_97fc_c6703437c018'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AntiLepton'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AntiLepton(
    
    class_iri='https://w3id.org/emmo#EMMO_716fadba_7ff8_4247_97fc_c6703437c018',
    
    class_name='AntiLepton',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_716fadba_7ff8_4247_97fc_c6703437c018',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AntiLepton',
        alias="class_name"
    )
    

    
    

    

    