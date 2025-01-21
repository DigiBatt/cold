
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturedMaterialModule import ManufacturedMaterial







class WovenMesh(ManufacturedMaterial):
    """
    Class representing the `WovenMesh` entity, which inherits from:
    - ManufacturedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3a69a00e_235a_4948_b369_8ac20116c85e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WovenMesh'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WovenMesh(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3a69a00e_235a_4948_b369_8ac20116c85e',
    
    class_name='WovenMesh',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3a69a00e_235a_4948_b369_8ac20116c85e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WovenMesh',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    