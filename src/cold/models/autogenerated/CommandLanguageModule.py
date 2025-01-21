
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConstructionLanguageModule import ConstructionLanguage







class CommandLanguage(ConstructionLanguage):
    """
    Class representing the `CommandLanguage` entity, which inherits from:
    - ConstructionLanguage

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c8fe15d0_caf7_46f7_883c_0e98081987f1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CommandLanguage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CommandLanguage(
    
    class_iri='https://w3id.org/emmo#EMMO_c8fe15d0_caf7_46f7_883c_0e98081987f1',
    
    class_name='CommandLanguage',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c8fe15d0_caf7_46f7_883c_0e98081987f1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CommandLanguage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    