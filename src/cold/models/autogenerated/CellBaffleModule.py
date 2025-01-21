
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComponentModule import Component







class CellBaffle(Component):
    """
    Class representing the `CellBaffle` entity, which inherits from:
    - Component

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_328c6e36_3706_4d92_abae_432fa3adb2a0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CellBaffle'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CellBaffle(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_328c6e36_3706_4d92_abae_432fa3adb2a0',
    
    class_name='CellBaffle',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_328c6e36_3706_4d92_abae_432fa3adb2a0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CellBaffle',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    