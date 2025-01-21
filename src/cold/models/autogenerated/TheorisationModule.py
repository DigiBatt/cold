
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeterminationModule import Determination



from .WholeModule import Whole



from .ProcessModule import Process





from .ObjectModule import Object





class Theorisation(Determination, Whole, Process):
    """
    Class representing the `Theorisation` entity, which inherits from:
    - Determination, Whole, Process

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6c739b1a_a774_4416_bb31_1961486fa9ed'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Theorisation'`
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
    obj = Theorisation(
    
    class_iri='https://w3id.org/emmo#EMMO_6c739b1a_a774_4416_bb31_1961486fa9ed',
    
    class_name='Theorisation',
    
    hasTemporaryParticipant="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6c739b1a_a774_4416_bb31_1961486fa9ed',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Theorisation',
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
    
    

    

    