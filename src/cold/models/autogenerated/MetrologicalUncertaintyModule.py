
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectivePropertyModule import ObjectiveProperty







class MetrologicalUncertainty(ObjectiveProperty):
    """
    Class representing the `MetrologicalUncertainty` entity, which inherits from:
    - ObjectiveProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_847724b7_acef_490e_9f0d_67da967f2812'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetrologicalUncertainty'`
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
    obj = MetrologicalUncertainty(
    
    class_iri='https://w3id.org/emmo#EMMO_847724b7_acef_490e_9f0d_67da967f2812',
    
    class_name='MetrologicalUncertainty',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_847724b7_acef_490e_9f0d_67da967f2812',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MetrologicalUncertainty',
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
    

    
    

    

    