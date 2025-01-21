
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialModule import Material







class FunctionallyDefinedMaterial(Material):
    """
    Class representing the `FunctionallyDefinedMaterial` entity, which inherits from:
    - Material

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8820f251_ad36_43f4_a693_c0e86a89cc1f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FunctionallyDefinedMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FunctionallyDefinedMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_8820f251_ad36_43f4_a693_c0e86a89cc1f',
    
    class_name='FunctionallyDefinedMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8820f251_ad36_43f4_a693_c0e86a89cc1f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FunctionallyDefinedMaterial',
        alias="class_name"
    )
    

    
    

    

    