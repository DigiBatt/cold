
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon





from .ParticipantModule import Participant





class ActiveMaterialParticleCracking(Whole, ElectrochemicalPhenomenon):
    """
    Class representing the `ActiveMaterialParticleCracking` entity, which inherits from:
    - Whole, ElectrochemicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6341d7d_7620_48f5_97b2_99b55c349169'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActiveMaterialParticleCracking'`
        - **Alias**: `class_name`
    
    - `hasParticipant` (`Optional[Participant]`): 
        - **Default Value**: `None`
        - **Alias**: `hasParticipant`
    
    - `isCauseOf` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `isCauseOf`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ActiveMaterialParticleCracking(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6341d7d_7620_48f5_97b2_99b55c349169',
    
    class_name='ActiveMaterialParticleCracking',
    
    hasParticipant="example_value",
    
    isCauseOf="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f6341d7d_7620_48f5_97b2_99b55c349169',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActiveMaterialParticleCracking',
        alias="class_name"
    )
    
    hasParticipant: Optional[Participant] = Field(
        None,
        alias="hasParticipant"
    )
    
    isCauseOf: Optional[str] = Field(
        None,
        alias="isCauseOf"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasParticipant", pre=True, always=True)
    def validate_hasParticipant(cls, value):
        if value is not None and not isinstance(value, Participant):
            raise ValueError(f"Field 'hasParticipant' must be an instance of 'Participant' or its subclass.")
        return value
    
    

    

    