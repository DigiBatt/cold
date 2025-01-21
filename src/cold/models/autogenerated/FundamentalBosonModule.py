
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StandardModelParticleModule import StandardModelParticle







class FundamentalBoson(StandardModelParticle):
    """
    Class representing the `FundamentalBoson` entity, which inherits from:
    - StandardModelParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fa3c9d4d_9fc9_4e8a_82c1_28c84e34133a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FundamentalBoson'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FundamentalBoson(
    
    class_iri='https://w3id.org/emmo#EMMO_fa3c9d4d_9fc9_4e8a_82c1_28c84e34133a',
    
    class_name='FundamentalBoson',
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fa3c9d4d_9fc9_4e8a_82c1_28c84e34133a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FundamentalBoson',
        alias="class_name"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    