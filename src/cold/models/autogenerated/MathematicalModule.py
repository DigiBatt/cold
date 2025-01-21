
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LanguageModule import Language







class Mathematical(Language):
    """
    Class representing the `Mathematical` entity, which inherits from:
    - Language

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_54ee6b5e_5261_44a8_86eb_5717e7fdb9d0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Mathematical'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Mathematical(
    
    class_iri='https://w3id.org/emmo#EMMO_54ee6b5e_5261_44a8_86eb_5717e7fdb9d0',
    
    class_name='Mathematical',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_54ee6b5e_5261_44a8_86eb_5717e7fdb9d0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Mathematical',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    