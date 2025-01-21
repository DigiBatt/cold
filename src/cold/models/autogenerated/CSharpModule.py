
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompiledLanguageModule import CompiledLanguage







class CSharp(CompiledLanguage):
    """
    Class representing the `CSharp` entity, which inherits from:
    - CompiledLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_268a8a97_3a6f_4022_93da_962a66827cdc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CSharp'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CSharp(
    
    class_iri='https://w3id.org/emmo#EMMO_268a8a97_3a6f_4022_93da_962a66827cdc',
    
    class_name='CSharp',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_268a8a97_3a6f_4022_93da_962a66827cdc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CSharp',
        alias="class_name"
    )
    

    
    

    

    