
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ParticulateMatterModule import ParticulateMatter



from .MatterModule import Matter



from .CompositePhysicalParticleModule import CompositePhysicalParticle







class Hadron(ParticulateMatter, Matter, CompositePhysicalParticle):
    """
    Class representing the `Hadron` entity, which inherits from:
    - ParticulateMatter, Matter, CompositePhysicalParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7b42954f_0b91_4b3a_a65e_2470202cf548'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Hadron'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Hadron(
    
    class_iri='https://w3id.org/emmo#EMMO_7b42954f_0b91_4b3a_a65e_2470202cf548',
    
    class_name='Hadron',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7b42954f_0b91_4b3a_a65e_2470202cf548',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Hadron',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    