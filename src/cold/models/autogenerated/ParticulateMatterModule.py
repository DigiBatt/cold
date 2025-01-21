
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MatterModule import Matter



from .CompositePhysicalParticleModule import CompositePhysicalParticle







class ParticulateMatter(Matter, CompositePhysicalParticle):
    """
    Class representing the `ParticulateMatter` entity, which inherits from:
    - Matter, CompositePhysicalParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_32f55395_8b94_40de_a103_bffa5c121d98'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ParticulateMatter'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ParticulateMatter(
    
    class_iri='https://w3id.org/emmo#EMMO_32f55395_8b94_40de_a103_bffa5c121d98',
    
    class_name='ParticulateMatter',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_32f55395_8b94_40de_a103_bffa5c121d98',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ParticulateMatter',
        alias="class_name"
    )
    

    
    

    

    