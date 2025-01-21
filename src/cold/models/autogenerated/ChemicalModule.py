
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LanguageModule import Language







class Chemical(Language):
    """
    Class representing the `Chemical` entity, which inherits from:
    - Language

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_abf7efbe_6b04_41b8_8326_4dd0f6be753e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Chemical'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Chemical(
    
    class_iri='https://w3id.org/emmo#EMMO_abf7efbe_6b04_41b8_8326_4dd0f6be753e',
    
    class_name='Chemical',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_abf7efbe_6b04_41b8_8326_4dd0f6be753e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Chemical',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    