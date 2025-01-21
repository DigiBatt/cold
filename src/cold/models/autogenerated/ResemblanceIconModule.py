
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IconModule import Icon







class ResemblanceIcon(Icon):
    """
    Class representing the `ResemblanceIcon` entity, which inherits from:
    - Icon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8c537c06_8e1d_4a3b_a251_1c89bb2c4790'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ResemblanceIcon'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ResemblanceIcon(
    
    class_iri='https://w3id.org/emmo#EMMO_8c537c06_8e1d_4a3b_a251_1c89bb2c4790',
    
    class_name='ResemblanceIcon',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8c537c06_8e1d_4a3b_a251_1c89bb2c4790',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ResemblanceIcon',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    