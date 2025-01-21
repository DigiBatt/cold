
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ComponentModule import Component







class Valve(Component):
    """
    Class representing the `Valve` entity, which inherits from:
    - Component

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a2f4dca3_829f_412b_9025_bd7581aad82a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Valve'`
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
    obj = Valve(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a2f4dca3_829f_412b_9025_bd7581aad82a',
    
    class_name='Valve',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a2f4dca3_829f_412b_9025_bd7581aad82a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Valve',
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
    

    
    

    

    