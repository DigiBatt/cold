
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ScriptingLanguageModule import ScriptingLanguage







class ApplicationSpecificScript(ScriptingLanguage):
    """
    Class representing the `ApplicationSpecificScript` entity, which inherits from:
    - ScriptingLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3c5b33a1_4f28_41f9_b725_1994df79bf55'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ApplicationSpecificScript'`
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
    obj = ApplicationSpecificScript(
    
    class_iri='https://w3id.org/emmo#EMMO_3c5b33a1_4f28_41f9_b725_1994df79bf55',
    
    class_name='ApplicationSpecificScript',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3c5b33a1_4f28_41f9_b725_1994df79bf55',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ApplicationSpecificScript',
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
    

    
    

    

    