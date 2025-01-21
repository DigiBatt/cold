
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ScriptingLanguageModule import ScriptingLanguage







class Python(ScriptingLanguage):
    """
    Class representing the `Python` entity, which inherits from:
    - ScriptingLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_add2e29d_6d87_4b78_9706_588e25557093'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Python'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Python(
    
    class_iri='https://w3id.org/emmo#EMMO_add2e29d_6d87_4b78_9706_588e25557093',
    
    class_name='Python',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_add2e29d_6d87_4b78_9706_588e25557093',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Python',
        alias="class_name"
    )
    

    
    

    

    