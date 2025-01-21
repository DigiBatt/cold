
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IconModule import Icon







class FunctionalIcon(Icon):
    """
    Class representing the `FunctionalIcon` entity, which inherits from:
    - Icon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c7013b53_3071_410b_a5e4_a8d266dcdfb5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FunctionalIcon'`
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
    obj = FunctionalIcon(
    
    class_iri='https://w3id.org/emmo#EMMO_c7013b53_3071_410b_a5e4_a8d266dcdfb5',
    
    class_name='FunctionalIcon',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c7013b53_3071_410b_a5e4_a8d266dcdfb5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FunctionalIcon',
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
    

    
    

    

    