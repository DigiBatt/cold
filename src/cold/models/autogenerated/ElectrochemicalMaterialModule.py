
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReactiveMaterialModule import ReactiveMaterial







class ElectrochemicalMaterial(ReactiveMaterial):
    """
    Class representing the `ElectrochemicalMaterial` entity, which inherits from:
    - ReactiveMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ebdb68e9_c4b5_4d57_a042_c0f51d446755'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalMaterial'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalMaterial(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ebdb68e9_c4b5_4d57_a042_c0f51d446755',
    
    class_name='ElectrochemicalMaterial',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ebdb68e9_c4b5_4d57_a042_c0f51d446755',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalMaterial',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    