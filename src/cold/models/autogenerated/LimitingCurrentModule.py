
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FaradaicCurrentModule import FaradaicCurrent







class LimitingCurrent(FaradaicCurrent):
    """
    Class representing the `LimitingCurrent` entity, which inherits from:
    - FaradaicCurrent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5ac8868_d318_4065_aa23_72140ae888ae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LimitingCurrent'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LimitingCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5ac8868_d318_4065_aa23_72140ae888ae',
    
    class_name='LimitingCurrent',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_d5ac8868_d318_4065_aa23_72140ae888ae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LimitingCurrent',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    