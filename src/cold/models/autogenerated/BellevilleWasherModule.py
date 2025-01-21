
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpringModule import Spring







class BellevilleWasher(Spring):
    """
    Class representing the `BellevilleWasher` entity, which inherits from:
    - Spring

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_98d5101e_cd11_4a0d_b856_6fcd8aad132e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BellevilleWasher'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BellevilleWasher(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_98d5101e_cd11_4a0d_b856_6fcd8aad132e',
    
    class_name='BellevilleWasher',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_98d5101e_cd11_4a0d_b856_6fcd8aad132e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BellevilleWasher',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    