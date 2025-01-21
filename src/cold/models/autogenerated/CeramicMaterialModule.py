
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ClassicallyDefinedMaterialModule import ClassicallyDefinedMaterial







class CeramicMaterial(ClassicallyDefinedMaterial):
    """
    Class representing the `CeramicMaterial` entity, which inherits from:
    - ClassicallyDefinedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c5e9e390_8836_4440_b4fd_c906fdd4f438'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CeramicMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CeramicMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_c5e9e390_8836_4440_b4fd_c906fdd4f438',
    
    class_name='CeramicMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c5e9e390_8836_4440_b4fd_c906fdd4f438',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CeramicMaterial',
        alias="class_name"
    )
    

    
    

    

    