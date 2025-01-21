
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeclarationModule import Declaration







class Naming(Declaration):
    """
    Class representing the `Naming` entity, which inherits from:
    - Declaration

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e999f9e0_7d63_4564_9028_07246580a267'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Naming'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Naming(
    
    class_iri='https://w3id.org/emmo#EMMO_e999f9e0_7d63_4564_9028_07246580a267',
    
    class_name='Naming',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e999f9e0_7d63_4564_9028_07246580a267',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Naming',
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
    

    
    

    

    