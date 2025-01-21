
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon





from .ParticipantModule import Participant





class Electrocatalysis(Whole, ElectrochemicalPhenomenon):
    """
    Class representing the `Electrocatalysis` entity, which inherits from:
    - Whole, ElectrochemicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d6f7f50_b343_4bd6_8612_2b8521a99c9b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electrocatalysis'`
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
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Electrocatalysis(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d6f7f50_b343_4bd6_8612_2b8521a99c9b',
    
    class_name='Electrocatalysis',
    
    hasParticipant="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4d6f7f50_b343_4bd6_8612_2b8521a99c9b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electrocatalysis',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    @validator("hasParticipant", pre=True, always=True)
    def validate_hasParticipant(cls, value):
        if value is not None and not isinstance(value, Participant):
            raise ValueError(f"Field 'hasParticipant' must be an instance of 'Participant' or its subclass.")
        return value
    
    

    

    