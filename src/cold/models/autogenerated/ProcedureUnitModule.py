
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetrologicalReferenceModule import MetrologicalReference







class ProcedureUnit(MetrologicalReference):
    """
    Class representing the `ProcedureUnit` entity, which inherits from:
    - MetrologicalReference

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c9c8f824_9127_4f93_bc21_69fe78a7f6f2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ProcedureUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ProcedureUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_c9c8f824_9127_4f93_bc21_69fe78a7f6f2',
    
    class_name='ProcedureUnit',
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c9c8f824_9127_4f93_bc21_69fe78a7f6f2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ProcedureUnit',
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
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    