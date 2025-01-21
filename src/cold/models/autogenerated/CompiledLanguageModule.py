
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProgrammingLanguageModule import ProgrammingLanguage







class CompiledLanguage(ProgrammingLanguage):
    """
    Class representing the `CompiledLanguage` entity, which inherits from:
    - ProgrammingLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1461e904_a2bf_4558_ad74_2706f5706b34'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CompiledLanguage'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CompiledLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_1461e904_a2bf_4558_ad74_2706f5706b34',
    
    class_name='CompiledLanguage',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1461e904_a2bf_4558_ad74_2706f5706b34',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CompiledLanguage',
        alias="class_name"
    )
    

    
    

    

    