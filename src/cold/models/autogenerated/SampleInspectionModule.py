
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CharacterisationProcedureModule import CharacterisationProcedure





from .ObjectModule import Object





class SampleInspection(CharacterisationProcedure):
    """
    Class representing the `SampleInspection` entity, which inherits from:
    - CharacterisationProcedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleInspection'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SampleInspection'`
        - **Alias**: `class_name`
    
    - `hasOutput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasOutput`
    
    - `hasTemporaryParticipant` (`Optional[Object]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTemporaryParticipant`
    
    - `hasInput` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasInput`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SampleInspection(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleInspection',
    
    class_name='SampleInspection',
    
    hasOutput="example_value",
    
    hasTemporaryParticipant="example_value",
    
    hasInput="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#SampleInspection',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SampleInspection',
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
    
    hasInput: Optional[str] = Field(
        None,
        alias="hasInput"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    @validator("hasTemporaryParticipant", pre=True, always=True)
    def validate_hasTemporaryParticipant(cls, value):
        if value is not None and not isinstance(value, Object):
            raise ValueError(f"Field 'hasTemporaryParticipant' must be an instance of 'Object' or its subclass.")
        return value
    
    

    

    