
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProcessModule import Process



from .NonTemporalRoleModule import NonTemporalRole







class ConstitutiveProcess(Process, NonTemporalRole):
    """
    Class representing the `ConstitutiveProcess` entity, which inherits from:
    - Process, NonTemporalRole

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f68858dd_64f4_4877_b7fb_70d04fbe5bab'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstitutiveProcess'`
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
    obj = ConstitutiveProcess(
    
    class_iri='https://w3id.org/emmo#EMMO_f68858dd_64f4_4877_b7fb_70d04fbe5bab',
    
    class_name='ConstitutiveProcess',
    
    elucidation="example_value",
    
    comment="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f68858dd_64f4_4877_b7fb_70d04fbe5bab',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstitutiveProcess',
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
    

    
    

    

    