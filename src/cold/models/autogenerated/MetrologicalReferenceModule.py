
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetrologicalModule import Metrological







class MetrologicalReference(Metrological):
    """
    Class representing the `MetrologicalReference` entity, which inherits from:
    - Metrological

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_18ce5200_00f5_45bb_8c6f_6fb128cd41ae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetrologicalReference'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MetrologicalReference(
    
    class_iri='https://w3id.org/emmo#EMMO_18ce5200_00f5_45bb_8c6f_6fb128cd41ae',
    
    class_name='MetrologicalReference',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_18ce5200_00f5_45bb_8c6f_6fb128cd41ae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MetrologicalReference',
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
    

    
    

    

    