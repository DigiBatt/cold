
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalParticleModule import CausalParticle



from .CausalStructureModule import CausalStructure







class CausalPath(CausalParticle, CausalStructure):
    """
    Class representing the `CausalPath` entity, which inherits from:
    - CausalParticle, CausalStructure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0f795e3e_c602_4577_9a43_d5a231aa1360'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CausalPath'`
        - **Alias**: `class_name`
    
    - `hasTemporalPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTemporalPart`
    
    - `OWLDLRestrictedAxiom` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `OWLDLRestrictedAxiom`
    
    - `conceptualisation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `conceptualisation`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CausalPath(
    
    class_iri='https://w3id.org/emmo#EMMO_0f795e3e_c602_4577_9a43_d5a231aa1360',
    
    class_name='CausalPath',
    
    hasTemporalPart="example_value",
    
    OWLDLRestrictedAxiom="example_value",
    
    conceptualisation="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0f795e3e_c602_4577_9a43_d5a231aa1360',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CausalPath',
        alias="class_name"
    )
    
    hasTemporalPart: Optional[str] = Field(
        None,
        alias="hasTemporalPart"
    )
    
    OWLDLRestrictedAxiom: Optional[str] = Field(
        None,
        alias="OWLDLRestrictedAxiom"
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
    

    
    

    

    