
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialLawModule import MaterialLaw







class KohlrauschsLaw(MaterialLaw):
    """
    Class representing the `KohlrauschsLaw` entity, which inherits from:
    - MaterialLaw

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_598ae3d0_76e9_429c_a0e1_8694525cb574'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'KohlrauschsLaw'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = KohlrauschsLaw(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_598ae3d0_76e9_429c_a0e1_8694525cb574',
    
    class_name='KohlrauschsLaw',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_598ae3d0_76e9_429c_a0e1_8694525cb574',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'KohlrauschsLaw',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    