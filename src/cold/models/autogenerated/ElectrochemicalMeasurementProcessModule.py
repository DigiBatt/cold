
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationMeasurementProcessModule import CharacterisationMeasurementProcess





from .ObjectModule import Object





class ElectrochemicalMeasurementProcess(CharacterisationMeasurementProcess):
    """
    Class representing the `ElectrochemicalMeasurementProcess` entity, which inherits from:
    - CharacterisationMeasurementProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f4ce4df2_d7e6_470f_8eab_3a911adaaf0f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalMeasurementProcess'`
        - **Alias**: `class_name`
    
    - `hasOutput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasOutput`
    
    - `hasTemporaryParticipant` (`Optional[Object]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTemporaryParticipant`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalMeasurementProcess(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f4ce4df2_d7e6_470f_8eab_3a911adaaf0f',
    
    class_name='ElectrochemicalMeasurementProcess',
    
    hasOutput="example_value",
    
    hasTemporaryParticipant="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f4ce4df2_d7e6_470f_8eab_3a911adaaf0f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalMeasurementProcess',
        alias="class_name"
    )
    
    hasOutput: Optional[str] = Field(
        None,
        alias="hasOutput"
    )
    
    hasTemporaryParticipant: Optional[Object] = Field(
        None,
        alias="hasTemporaryParticipant"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasTemporaryParticipant", pre=True, always=True)
    def validate_hasTemporaryParticipant(cls, value):
        if value is not None and not isinstance(value, Object):
            raise ValueError(f"Field 'hasTemporaryParticipant' must be an instance of 'Object' or its subclass.")
        return value
    
    

    

    