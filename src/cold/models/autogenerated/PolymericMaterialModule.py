
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ClassicallyDefinedMaterialModule import ClassicallyDefinedMaterial







class PolymericMaterial(ClassicallyDefinedMaterial):
    """
    Class representing the `PolymericMaterial` entity, which inherits from:
    - ClassicallyDefinedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fb27e6d6_159e_48a6_9c29_76dc31d8a860'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PolymericMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PolymericMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_fb27e6d6_159e_48a6_9c29_76dc31d8a860',
    
    class_name='PolymericMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fb27e6d6_159e_48a6_9c29_76dc31d8a860',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PolymericMaterial',
        alias="class_name"
    )
    

    
    

    

    