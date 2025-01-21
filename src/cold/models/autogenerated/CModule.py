
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompiledLanguageModule import CompiledLanguage







class C(CompiledLanguage):
    """
    Class representing the `C` entity, which inherits from:
    - CompiledLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_36a9bf69_483b_42fd_8a0c_7ac9206320bc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'C'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = C(
    
    class_iri='https://w3id.org/emmo#EMMO_36a9bf69_483b_42fd_8a0c_7ac9206320bc',
    
    class_name='C',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_36a9bf69_483b_42fd_8a0c_7ac9206320bc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'C',
        alias="class_name"
    )
    

    
    

    

    