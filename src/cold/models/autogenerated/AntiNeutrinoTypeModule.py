
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RightHandedParticleModule import RightHandedParticle



from .AntiLeptonModule import AntiLepton







class AntiNeutrinoType(RightHandedParticle, AntiLepton):
    """
    Class representing the `AntiNeutrinoType` entity, which inherits from:
    - RightHandedParticle, AntiLepton

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_edfa7d90_6b21_4669_b9b1_13c77de760eb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AntiNeutrinoType'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AntiNeutrinoType(
    
    class_iri='https://w3id.org/emmo#EMMO_edfa7d90_6b21_4669_b9b1_13c77de760eb',
    
    class_name='AntiNeutrinoType',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_edfa7d90_6b21_4669_b9b1_13c77de760eb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AntiNeutrinoType',
        alias="class_name"
    )
    

    
    

    

    