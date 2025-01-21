
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LanguageModule import Language







class ComputerScience(Language):
    """
    Class representing the `ComputerScience` entity, which inherits from:
    - Language

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b45fbdc6_2519_4885_aa49_c56b394c3910'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ComputerScience'`
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
    obj = ComputerScience(
    
    class_iri='https://w3id.org/emmo#EMMO_b45fbdc6_2519_4885_aa49_c56b394c3910',
    
    class_name='ComputerScience',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b45fbdc6_2519_4885_aa49_c56b394c3910',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ComputerScience',
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
    

    
    

    

    