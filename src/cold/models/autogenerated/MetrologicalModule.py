
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LanguageModule import Language







class Metrological(Language):
    """
    Class representing the `Metrological` entity, which inherits from:
    - Language

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_985bec21_989f_4b9e_a4b3_735d88099c3c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Metrological'`
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
    obj = Metrological(
    
    class_iri='https://w3id.org/emmo#EMMO_985bec21_989f_4b9e_a4b3_735d88099c3c',
    
    class_name='Metrological',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_985bec21_989f_4b9e_a4b3_735d88099c3c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Metrological',
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
    

    
    

    

    