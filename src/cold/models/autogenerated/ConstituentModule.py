
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectModule import Object



from .NonTemporalRoleModule import NonTemporalRole







class Constituent(Object, NonTemporalRole):
    """
    Class representing the `Constituent` entity, which inherits from:
    - Object, NonTemporalRole

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ceaaf9f7_fd11_424b_8fda_9afa186af186'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Constituent'`
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
    obj = Constituent(
    
    class_iri='https://w3id.org/emmo#EMMO_ceaaf9f7_fd11_424b_8fda_9afa186af186',
    
    class_name='Constituent',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ceaaf9f7_fd11_424b_8fda_9afa186af186',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Constituent',
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
    

    
    

    

    