
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompiledLanguageModule import CompiledLanguage







class CPlusPlus(CompiledLanguage):
    """
    Class representing the `CPlusPlus` entity, which inherits from:
    - CompiledLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_64aba1e5_24b7_4140_8eb4_676c35698e79'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CPlusPlus'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CPlusPlus(
    
    class_iri='https://w3id.org/emmo#EMMO_64aba1e5_24b7_4140_8eb4_676c35698e79',
    
    class_name='CPlusPlus',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_64aba1e5_24b7_4140_8eb4_676c35698e79',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CPlusPlus',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    