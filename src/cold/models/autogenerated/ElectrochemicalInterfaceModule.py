
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InterfaceModule import Interface







class ElectrochemicalInterface(Interface):
    """
    Class representing the `ElectrochemicalInterface` entity, which inherits from:
    - Interface

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50044b99_b858_433b_a32d_23d1e1cf88b2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalInterface'`
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
    obj = ElectrochemicalInterface(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50044b99_b858_433b_a32d_23d1e1cf88b2',
    
    class_name='ElectrochemicalInterface',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_50044b99_b858_433b_a32d_23d1e1cf88b2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalInterface',
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
    

    
    

    

    