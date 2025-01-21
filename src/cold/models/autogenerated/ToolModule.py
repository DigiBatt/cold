
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ParticipantModule import Participant



from .ObjectModule import Object







class Tool(Participant, Object):
    """
    Class representing the `Tool` entity, which inherits from:
    - Participant, Object

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5c68497d_2544_4cd4_897b_1ea783c9f6fe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Tool'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Tool(
    
    class_iri='https://w3id.org/emmo#EMMO_5c68497d_2544_4cd4_897b_1ea783c9f6fe',
    
    class_name='Tool',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5c68497d_2544_4cd4_897b_1ea783c9f6fe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Tool',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    