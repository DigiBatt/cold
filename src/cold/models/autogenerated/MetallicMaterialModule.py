
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ClassicallyDefinedMaterialModule import ClassicallyDefinedMaterial







class MetallicMaterial(ClassicallyDefinedMaterial):
    """
    Class representing the `MetallicMaterial` entity, which inherits from:
    - ClassicallyDefinedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4c1f58cd_6e2c_48fb_8098_1cbb762abb05'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetallicMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MetallicMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_4c1f58cd_6e2c_48fb_8098_1cbb762abb05',
    
    class_name='MetallicMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4c1f58cd_6e2c_48fb_8098_1cbb762abb05',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MetallicMaterial',
        alias="class_name"
    )
    

    
    

    

    