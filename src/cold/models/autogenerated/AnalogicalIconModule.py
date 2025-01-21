
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IconModule import Icon







class AnalogicalIcon(Icon):
    """
    Class representing the `AnalogicalIcon` entity, which inherits from:
    - Icon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4f2d1fcc_e20c_4479_9ad7_7a0480dd3e44'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AnalogicalIcon'`
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
    obj = AnalogicalIcon(
    
    class_iri='https://w3id.org/emmo#EMMO_4f2d1fcc_e20c_4479_9ad7_7a0480dd3e44',
    
    class_name='AnalogicalIcon',
    
    elucidation="example_value",
    
    comment="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4f2d1fcc_e20c_4479_9ad7_7a0480dd3e44',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AnalogicalIcon',
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
    

    
    

    

    