
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemporalRoleModule import TemporalRole



from .ProcessModule import Process







class Stage(TemporalRole, Process):
    """
    Class representing the `Stage` entity, which inherits from:
    - TemporalRole, Process

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a633c6f8_4269_4870_9b28_f5ca1783fd54'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Stage'`
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
    obj = Stage(
    
    class_iri='https://w3id.org/emmo#EMMO_a633c6f8_4269_4870_9b28_f5ca1783fd54',
    
    class_name='Stage',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a633c6f8_4269_4870_9b28_f5ca1783fd54',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Stage',
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
    

    
    

    

    