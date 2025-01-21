
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AdditiveModule import Additive







class ConductiveAdditive(Additive):
    """
    Class representing the `ConductiveAdditive` entity, which inherits from:
    - Additive

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_82fef384_8eec_4765_b707_5397054df594'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConductiveAdditive'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConductiveAdditive(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_82fef384_8eec_4765_b707_5397054df594',
    
    class_name='ConductiveAdditive',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_82fef384_8eec_4765_b707_5397054df594',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConductiveAdditive',
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
    

    
    

    

    