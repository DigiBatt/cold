
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ScriptingLanguageModule import ScriptingLanguage







class Ruby(ScriptingLanguage):
    """
    Class representing the `Ruby` entity, which inherits from:
    - ScriptingLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_53dd6f2a_f9de_4f83_b925_1bf39a4ab9a6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Ruby'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Ruby(
    
    class_iri='https://w3id.org/emmo#EMMO_53dd6f2a_f9de_4f83_b925_1bf39a4ab9a6',
    
    class_name='Ruby',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_53dd6f2a_f9de_4f83_b925_1bf39a4ab9a6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Ruby',
        alias="class_name"
    )
    

    
    

    

    