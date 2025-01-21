
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TechnologyProcessModule import TechnologyProcess





from .ObjectModule import Object





class Manufacturing(TechnologyProcess):
    """
    Class representing the `Manufacturing` entity, which inherits from:
    - TechnologyProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a4d66059_5dd3_4b90_b4cb_10960559441b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Manufacturing'`
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
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Manufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_a4d66059_5dd3_4b90_b4cb_10960559441b',
    
    class_name='Manufacturing',
    
    hasOutput="example_value",
    
    hasTemporaryParticipant="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a4d66059_5dd3_4b90_b4cb_10960559441b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Manufacturing',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    @validator("hasTemporaryParticipant", pre=True, always=True)
    def validate_hasTemporaryParticipant(cls, value):
        if value is not None and not isinstance(value, Object):
            raise ValueError(f"Field 'hasTemporaryParticipant' must be an instance of 'Object' or its subclass.")
        return value
    
    

    

    