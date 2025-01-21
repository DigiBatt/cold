
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StandardModelParticleModule import StandardModelParticle







class FundamentalFermion(StandardModelParticle):
    """
    Class representing the `FundamentalFermion` entity, which inherits from:
    - StandardModelParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8dbaf3ca_8f0d_4c45_92e1_c6d805b83c87'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FundamentalFermion'`
        - **Alias**: `class_name`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FundamentalFermion(
    
    class_iri='https://w3id.org/emmo#EMMO_8dbaf3ca_8f0d_4c45_92e1_c6d805b83c87',
    
    class_name='FundamentalFermion',
    
    conceptualisation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8dbaf3ca_8f0d_4c45_92e1_c6d805b83c87',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FundamentalFermion',
        alias="class_name"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    