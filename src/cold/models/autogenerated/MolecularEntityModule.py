
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ParticulateMatterModule import ParticulateMatter



from .ChemicalEntityModule import ChemicalEntity



from .CompositePhysicalParticleModule import CompositePhysicalParticle



from .MatterModule import Matter







class MolecularEntity(ParticulateMatter, ChemicalEntity, CompositePhysicalParticle, Matter):
    """
    Class representing the `MolecularEntity` entity, which inherits from:
    - ParticulateMatter, ChemicalEntity, CompositePhysicalParticle, Matter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_21205421_5783_4d3e_81e5_10c5d894a88a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MolecularEntity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MolecularEntity(
    
    class_iri='https://w3id.org/emmo#EMMO_21205421_5783_4d3e_81e5_10c5d894a88a',
    
    class_name='MolecularEntity',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_21205421_5783_4d3e_81e5_10c5d894a88a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MolecularEntity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    