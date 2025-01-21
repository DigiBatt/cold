
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConstituentModule import Constituent







class ElectrochemicalConstituent(Constituent):
    """
    Class representing the `ElectrochemicalConstituent` entity, which inherits from:
    - Constituent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b5ea31c9_bb10_4276_980e_c3eceb1efc82'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalConstituent'`
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
    obj = ElectrochemicalConstituent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b5ea31c9_bb10_4276_980e_c3eceb1efc82',
    
    class_name='ElectrochemicalConstituent',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b5ea31c9_bb10_4276_980e_c3eceb1efc82',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalConstituent',
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
    

    
    

    

    