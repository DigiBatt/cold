
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalDegradationPhenomenonModule import ElectrochemicalDegradationPhenomenon





from .ParticipantModule import Participant





class CapacityFade(ElectrochemicalDegradationPhenomenon):
    """
    Class representing the `CapacityFade` entity, which inherits from:
    - ElectrochemicalDegradationPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e3d3d21c_cb9a_498c_bdb0_63c964f0d3c6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CapacityFade'`
        - **Alias**: `class_name`
    
    - `hasParticipant` (`Optional[Participant]`): 
        - **Default Value**: `None`
        - **Alias**: `hasParticipant`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CapacityFade(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e3d3d21c_cb9a_498c_bdb0_63c964f0d3c6',
    
    class_name='CapacityFade',
    
    hasParticipant="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e3d3d21c_cb9a_498c_bdb0_63c964f0d3c6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CapacityFade',
        alias="class_name"
    )
    
    hasParticipant: Optional[Participant] = Field(
        None,
        alias="hasParticipant"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasParticipant", pre=True, always=True)
    def validate_hasParticipant(cls, value):
        if value is not None and not isinstance(value, Participant):
            raise ValueError(f"Field 'hasParticipant' must be an instance of 'Participant' or its subclass.")
        return value
    
    

    

    