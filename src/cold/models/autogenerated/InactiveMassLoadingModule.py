
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MassLoadingModule import MassLoading







class InactiveMassLoading(MassLoading):
    """
    Class representing the `InactiveMassLoading` entity, which inherits from:
    - MassLoading

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2cfea66b_756d_4642_986f_9a41abbd7034'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InactiveMassLoading'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InactiveMassLoading(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2cfea66b_756d_4642_986f_9a41abbd7034',
    
    class_name='InactiveMassLoading',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2cfea66b_756d_4642_986f_9a41abbd7034',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InactiveMassLoading',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    