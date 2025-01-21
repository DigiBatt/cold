
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltageControlledProcessModule import VoltageControlledProcess





from .ObjectModule import Object





class VoltageHold(VoltageControlledProcess):
    """
    Class representing the `VoltageHold` entity, which inherits from:
    - VoltageControlledProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f07be701_9d6a_415b_ac6d_63202297a7a1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VoltageHold'`
        - **Alias**: `class_name`
    
    - `hasTemporaryParticipant` (`Optional[Object]`): 
        - **Default Value**: `None`
        - **Alias**: `hasTemporaryParticipant`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VoltageHold(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f07be701_9d6a_415b_ac6d_63202297a7a1',
    
    class_name='VoltageHold',
    
    hasTemporaryParticipant="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f07be701_9d6a_415b_ac6d_63202297a7a1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VoltageHold',
        alias="class_name"
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
    
    

    

    