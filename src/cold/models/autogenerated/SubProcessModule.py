
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProcessModule import Process



from .NonTemporalRoleModule import NonTemporalRole







class SubProcess(Process, NonTemporalRole):
    """
    Class representing the `SubProcess` entity, which inherits from:
    - Process, NonTemporalRole

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_49804605_c0fe_4538_abda_f70ba1dc8a5d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SubProcess'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SubProcess(
    
    class_iri='https://w3id.org/emmo#EMMO_49804605_c0fe_4538_abda_f70ba1dc8a5d',
    
    class_name='SubProcess',
    
    elucidation="example_value",
    
    comment="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_49804605_c0fe_4538_abda_f70ba1dc8a5d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SubProcess',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    