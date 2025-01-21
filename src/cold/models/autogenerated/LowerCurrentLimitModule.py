
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentLimitModule import CurrentLimit







class LowerCurrentLimit(CurrentLimit):
    """
    Class representing the `LowerCurrentLimit` entity, which inherits from:
    - CurrentLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7db845e7_0e5b_47d4_b954_2a2b8e85deea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LowerCurrentLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LowerCurrentLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7db845e7_0e5b_47d4_b954_2a2b8e85deea',
    
    class_name='LowerCurrentLimit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_7db845e7_0e5b_47d4_b954_2a2b8e85deea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LowerCurrentLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    