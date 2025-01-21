
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DoubleLayerModelModule import DoubleLayerModel







class SternModel(DoubleLayerModel):
    """
    Class representing the `SternModel` entity, which inherits from:
    - DoubleLayerModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aa5ed981_c11b_4c4f_b1fd_8c432e009484'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SternModel'`
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
    obj = SternModel(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aa5ed981_c11b_4c4f_b1fd_8c432e009484',
    
    class_name='SternModel',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_aa5ed981_c11b_4c4f_b1fd_8c432e009484',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SternModel',
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
    

    
    

    

    