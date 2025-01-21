
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon





from .ParticipantModule import Participant





class InterphaseGrowth(Whole, ElectrochemicalPhenomenon):
    """
    Class representing the `InterphaseGrowth` entity, which inherits from:
    - Whole, ElectrochemicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_402598d9_0eea_405d_b0d0_3b8b79deba6f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InterphaseGrowth'`
        - **Alias**: `class_name`
    
    - `hasParticipant` (`Optional[Participant]`): 
        - **Default Value**: `None`
        - **Alias**: `hasParticipant`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InterphaseGrowth(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_402598d9_0eea_405d_b0d0_3b8b79deba6f',
    
    class_name='InterphaseGrowth',
    
    hasParticipant="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_402598d9_0eea_405d_b0d0_3b8b79deba6f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InterphaseGrowth',
        alias="class_name"
    )
    
    hasParticipant: Optional[Participant] = Field(
        None,
        alias="hasParticipant"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    @validator("hasParticipant", pre=True, always=True)
    def validate_hasParticipant(cls, value):
        if value is not None and not isinstance(value, Participant):
            raise ValueError(f"Field 'hasParticipant' must be an instance of 'Participant' or its subclass.")
        return value
    
    

    

    