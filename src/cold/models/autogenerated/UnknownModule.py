
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumericalVariableModule import NumericalVariable







class Unknown(NumericalVariable):
    """
    Class representing the `Unknown` entity, which inherits from:
    - NumericalVariable

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fe7e56ce_118b_4243_9aad_20eb9f4f31f6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Unknown'`
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
    obj = Unknown(
    
    class_iri='https://w3id.org/emmo#EMMO_fe7e56ce_118b_4243_9aad_20eb9f4f31f6',
    
    class_name='Unknown',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fe7e56ce_118b_4243_9aad_20eb9f4f31f6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Unknown',
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
    

    
    

    

    