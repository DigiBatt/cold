
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TerminalModule import Terminal







class NegativeTerminal(Terminal):
    """
    Class representing the `NegativeTerminal` entity, which inherits from:
    - Terminal

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b851c7e9_60bf_4d3d_abe1_8d08d3d85124'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NegativeTerminal'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `contacts` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `contacts`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NegativeTerminal(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b851c7e9_60bf_4d3d_abe1_8d08d3d85124',
    
    class_name='NegativeTerminal',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    contacts="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b851c7e9_60bf_4d3d_abe1_8d08d3d85124',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NegativeTerminal',
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
    
    contacts: Optional[str] = Field(
        None,
        alias="contacts"
    )
    

    
    

    

    