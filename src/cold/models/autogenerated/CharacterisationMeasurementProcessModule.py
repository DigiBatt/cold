
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MeasurementModule import Measurement



from .CharacterisationProcedureModule import CharacterisationProcedure





from .ObjectModule import Object





class CharacterisationMeasurementProcess(Measurement, CharacterisationProcedure):
    """
    Class representing the `CharacterisationMeasurementProcess` entity, which inherits from:
    - Measurement, CharacterisationProcedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementProcess'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationMeasurementProcess'`
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
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `VIMTerm` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `VIMTerm`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationMeasurementProcess(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementProcess',
    
    class_name='CharacterisationMeasurementProcess',
    
    hasOutput="example_value",
    
    hasTemporaryParticipant="example_value",
    
    hasInput="example_value",
    
    definition="example_value",
    
    elucidation="example_value",
    
    VIMTerm="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationMeasurementProcess',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationMeasurementProcess',
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
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    VIMTerm: Optional[str] = Field(
        None,
        alias="VIMTerm"
    )
    

    
    @validator("hasTemporaryParticipant", pre=True, always=True)
    def validate_hasTemporaryParticipant(cls, value):
        if value is not None and not isinstance(value, Object):
            raise ValueError(f"Field 'hasTemporaryParticipant' must be an instance of 'Object' or its subclass.")
        return value
    
    

    

    