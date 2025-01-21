
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalParticleModule import CausalParticle







class Quantum(CausalParticle):
    """
    Class representing the `Quantum` entity, which inherits from:
    - CausalParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3f9ae00e_810c_4518_aec2_7200e424cf68'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Quantum'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
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
    obj = Quantum(
    
    class_iri='https://w3id.org/emmo#EMMO_3f9ae00e_810c_4518_aec2_7200e424cf68',
    
    class_name='Quantum',
    
    definition="example_value",
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3f9ae00e_810c_4518_aec2_7200e424cf68',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Quantum',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    conceptualisation: Optional[str] = Field(
        None,
        alias="conceptualisation"
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
    

    
    

    

    