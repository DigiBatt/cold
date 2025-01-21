
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ScriptingLanguageModule import ScriptingLanguage







class JavaScript(ScriptingLanguage):
    """
    Class representing the `JavaScript` entity, which inherits from:
    - ScriptingLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_161bef57_cc59_4246_8249_19dbdae96e7b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'JavaScript'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = JavaScript(
    
    class_iri='https://w3id.org/emmo#EMMO_161bef57_cc59_4246_8249_19dbdae96e7b',
    
    class_name='JavaScript',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_161bef57_cc59_4246_8249_19dbdae96e7b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'JavaScript',
        alias="class_name"
    )
    

    
    

    

    