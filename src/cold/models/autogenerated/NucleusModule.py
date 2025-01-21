
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ParticulateMatterModule import ParticulateMatter



from .MatterModule import Matter



from .CompositePhysicalParticleModule import CompositePhysicalParticle







class Nucleus(ParticulateMatter, Matter, CompositePhysicalParticle):
    """
    Class representing the `Nucleus` entity, which inherits from:
    - ParticulateMatter, Matter, CompositePhysicalParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f835f4d4_c665_403d_ab25_dca5cc74be52'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Nucleus'`
        - **Alias**: `class_name`
    
    - `hasPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Nucleus(
    
    class_iri='https://w3id.org/emmo#EMMO_f835f4d4_c665_403d_ab25_dca5cc74be52',
    
    class_name='Nucleus',
    
    hasPart="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f835f4d4_c665_403d_ab25_dca5cc74be52',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Nucleus',
        alias="class_name"
    )
    
    hasPart: Optional[str] = Field(
        None,
        alias="hasPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    