
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CaseModule import Case







class PouchCase(Case):
    """
    Class representing the `PouchCase` entity, which inherits from:
    - Case

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74459386_875c_4303_b774_60125b599d06'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PouchCase'`
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
    obj = PouchCase(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74459386_875c_4303_b774_60125b599d06',
    
    class_name='PouchCase',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_74459386_875c_4303_b774_60125b599d06',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PouchCase',
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
    

    
    

    

    