
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ClassicallyDefinedMaterialModule import ClassicallyDefinedMaterial







class AmorphousMaterial(ClassicallyDefinedMaterial):
    """
    Class representing the `AmorphousMaterial` entity, which inherits from:
    - ClassicallyDefinedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0afc19b0_2d43_4b3d_8da0_9ffb63bc1492'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmorphousMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmorphousMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_0afc19b0_2d43_4b3d_8da0_9ffb63bc1492',
    
    class_name='AmorphousMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0afc19b0_2d43_4b3d_8da0_9ffb63bc1492',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmorphousMaterial',
        alias="class_name"
    )
    

    
    

    

    