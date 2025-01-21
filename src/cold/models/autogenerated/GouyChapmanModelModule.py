
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DoubleLayerModelModule import DoubleLayerModel







class GouyChapmanModel(DoubleLayerModel):
    """
    Class representing the `GouyChapmanModel` entity, which inherits from:
    - DoubleLayerModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa54f95d_b49e_43b5_84c3_35520d0fb2f6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'GouyChapmanModel'`
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
    obj = GouyChapmanModel(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa54f95d_b49e_43b5_84c3_35520d0fb2f6',
    
    class_name='GouyChapmanModel',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa54f95d_b49e_43b5_84c3_35520d0fb2f6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'GouyChapmanModel',
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
    

    
    

    

    