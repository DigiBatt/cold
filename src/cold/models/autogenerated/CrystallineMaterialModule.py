
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ClassicallyDefinedMaterialModule import ClassicallyDefinedMaterial







class CrystallineMaterial(ClassicallyDefinedMaterial):
    """
    Class representing the `CrystallineMaterial` entity, which inherits from:
    - ClassicallyDefinedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f1025834_0cd2_42a1_bfeb_13bec41c8655'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CrystallineMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CrystallineMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_f1025834_0cd2_42a1_bfeb_13bec41c8655',
    
    class_name='CrystallineMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f1025834_0cd2_42a1_bfeb_13bec41c8655',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CrystallineMaterial',
        alias="class_name"
    )
    

    
    

    

    