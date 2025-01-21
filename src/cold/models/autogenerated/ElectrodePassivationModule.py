
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon





from .ParticipantModule import Participant





class ElectrodePassivation(Whole, ElectrochemicalPhenomenon):
    """
    Class representing the `ElectrodePassivation` entity, which inherits from:
    - Whole, ElectrochemicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_01260656_ac32_472e_9513_a607366538ec'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrodePassivation'`
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
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrodePassivation(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_01260656_ac32_472e_9513_a607366538ec',
    
    class_name='ElectrodePassivation',
    
    hasParticipant="example_value",
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_01260656_ac32_472e_9513_a607366538ec',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrodePassivation',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasParticipant", pre=True, always=True)
    def validate_hasParticipant(cls, value):
        if value is not None and not isinstance(value, Participant):
            raise ValueError(f"Field 'hasParticipant' must be an instance of 'Participant' or its subclass.")
        return value
    
    

    

    