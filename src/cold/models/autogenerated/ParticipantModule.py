
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectModule import Object



from .NonTemporalRoleModule import NonTemporalRole







class Participant(Object, NonTemporalRole):
    """
    Class representing the `Participant` entity, which inherits from:
    - Object, NonTemporalRole

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_13191289_6c2b_4741_93e1_82d53bd0e703'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Participant'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Participant(
    
    class_iri='https://w3id.org/emmo#EMMO_13191289_6c2b_4741_93e1_82d53bd0e703',
    
    class_name='Participant',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_13191289_6c2b_4741_93e1_82d53bd0e703',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Participant',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    