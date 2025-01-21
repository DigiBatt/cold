
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompiledLanguageModule import CompiledLanguage







class Java(CompiledLanguage):
    """
    Class representing the `Java` entity, which inherits from:
    - CompiledLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_09007bc0_b5f2_4fb9_af01_caf948cf2044'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Java'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Java(
    
    class_iri='https://w3id.org/emmo#EMMO_09007bc0_b5f2_4fb9_af01_caf948cf2044',
    
    class_name='Java',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_09007bc0_b5f2_4fb9_af01_caf948cf2044',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Java',
        alias="class_name"
    )
    

    
    

    

    