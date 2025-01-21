
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MathematicalModelModule import MathematicalModel







class PostProcessingModel(MathematicalModel):
    """
    Class representing the `PostProcessingModel` entity, which inherits from:
    - MathematicalModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PostProcessingModel'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PostProcessingModel'`
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
    obj = PostProcessingModel(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#PostProcessingModel',
    
    class_name='PostProcessingModel',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#PostProcessingModel',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PostProcessingModel',
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
    

    
    

    

    