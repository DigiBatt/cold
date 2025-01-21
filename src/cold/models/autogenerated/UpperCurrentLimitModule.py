
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentLimitModule import CurrentLimit







class UpperCurrentLimit(CurrentLimit):
    """
    Class representing the `UpperCurrentLimit` entity, which inherits from:
    - CurrentLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3dac5115_6337_40a6_a2ab_317087fe3b45'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UpperCurrentLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UpperCurrentLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3dac5115_6337_40a6_a2ab_317087fe3b45',
    
    class_name='UpperCurrentLimit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3dac5115_6337_40a6_a2ab_317087fe3b45',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UpperCurrentLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    