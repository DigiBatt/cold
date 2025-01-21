
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SideReactionModule import SideReaction







class ParasiticReaction(SideReaction):
    """
    Class representing the `ParasiticReaction` entity, which inherits from:
    - SideReaction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b79d4f9e_5727_4895_8d7f_5fc18d83eb90'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ParasiticReaction'`
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
    obj = ParasiticReaction(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b79d4f9e_5727_4895_8d7f_5fc18d83eb90',
    
    class_name='ParasiticReaction',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b79d4f9e_5727_4895_8d7f_5fc18d83eb90',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ParasiticReaction',
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
    

    
    

    

    