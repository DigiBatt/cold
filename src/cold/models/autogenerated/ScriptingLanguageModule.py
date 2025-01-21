
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProgrammingLanguageModule import ProgrammingLanguage







class ScriptingLanguage(ProgrammingLanguage):
    """
    Class representing the `ScriptingLanguage` entity, which inherits from:
    - ProgrammingLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f84b1b92_1dc8_4146_99f0_b03cd53e455b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ScriptingLanguage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ScriptingLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_f84b1b92_1dc8_4146_99f0_b03cd53e455b',
    
    class_name='ScriptingLanguage',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f84b1b92_1dc8_4146_99f0_b03cd53e455b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ScriptingLanguage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    