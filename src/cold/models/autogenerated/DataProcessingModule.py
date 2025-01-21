
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComputationModule import Computation





from .ParticipantModule import Participant





class DataProcessing(Computation):
    """
    Class representing the `DataProcessing` entity, which inherits from:
    - Computation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1c7f2dfe_0db4_4bf6_a0f6_853054a34ead'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DataProcessing'`
        - **Alias**: `class_name`
    
    - `hasOutput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasOutput`
    
    - `hasInput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasInput`
    
    - `hasParticipant` (`Optional[Participant]`): 
        - **Default Value**: `None`
        - **Alias**: `hasParticipant`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DataProcessing(
    
    class_iri='https://w3id.org/emmo#EMMO_1c7f2dfe_0db4_4bf6_a0f6_853054a34ead',
    
    class_name='DataProcessing',
    
    hasOutput="example_value",
    
    hasInput="example_value",
    
    hasParticipant="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1c7f2dfe_0db4_4bf6_a0f6_853054a34ead',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DataProcessing',
        alias="class_name"
    )
    
    hasOutput: Optional[str] = Field(
        None,
        alias="hasOutput"
    )
    
    hasInput: Optional[str] = Field(
        None,
        alias="hasInput"
    )
    
    hasParticipant: Optional[Participant] = Field(
        None,
        alias="hasParticipant"
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
    
    

    

    