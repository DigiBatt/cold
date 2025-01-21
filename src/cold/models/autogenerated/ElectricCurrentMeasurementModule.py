
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementModule import Measurement





from .ParticipantModule import Participant





class ElectricCurrentMeasurement(Measurement):
    """
    Class representing the `ElectricCurrentMeasurement` entity, which inherits from:
    - Measurement

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_158ae038_c64b_4cc0_aa56_650475490705'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectricCurrentMeasurement'`
        - **Alias**: `class_name`
    
    - `hasOutput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasOutput`
    
    - `hasParticipant` (`Optional[Participant]`): 
        - **Default Value**: `None`
        - **Alias**: `hasParticipant`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectricCurrentMeasurement(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_158ae038_c64b_4cc0_aa56_650475490705',
    
    class_name='ElectricCurrentMeasurement',
    
    hasOutput="example_value",
    
    hasParticipant="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_158ae038_c64b_4cc0_aa56_650475490705',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectricCurrentMeasurement',
        alias="class_name"
    )
    
    hasOutput: Optional[str] = Field(
        None,
        alias="hasOutput"
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
    
    

    

    