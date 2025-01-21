
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicalParticleModule import PhysicalParticle







class Boson(PhysicalParticle):
    """
    Class representing the `Boson` entity, which inherits from:
    - PhysicalParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b5a5494c_83bf_44aa_a9a6_49b948e68939'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Boson'`
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
    obj = Boson(
    
    class_iri='https://w3id.org/emmo#EMMO_b5a5494c_83bf_44aa_a9a6_49b948e68939',
    
    class_name='Boson',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b5a5494c_83bf_44aa_a9a6_49b948e68939',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Boson',
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
    

    
    

    

    