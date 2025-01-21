
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompositePhysicalParticleModule import CompositePhysicalParticle



from .BosonModule import Boson







class CompositeBoson(CompositePhysicalParticle, Boson):
    """
    Class representing the `CompositeBoson` entity, which inherits from:
    - CompositePhysicalParticle, Boson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1f19b65b_35bf_4662_a318_7f1c147cb3b6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CompositeBoson'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CompositeBoson(
    
    class_iri='https://w3id.org/emmo#EMMO_1f19b65b_35bf_4662_a318_7f1c147cb3b6',
    
    class_name='CompositeBoson',
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1f19b65b_35bf_4662_a318_7f1c147cb3b6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CompositeBoson',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    