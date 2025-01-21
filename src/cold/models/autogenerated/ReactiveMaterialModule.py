
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicallyDefinedMaterialModule import ChemicallyDefinedMaterial







class ReactiveMaterial(ChemicallyDefinedMaterial):
    """
    Class representing the `ReactiveMaterial` entity, which inherits from:
    - ChemicallyDefinedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_68390bfb_e307_479d_8f78_d66d8773cb1d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ReactiveMaterial'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ReactiveMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_68390bfb_e307_479d_8f78_d66d8773cb1d',
    
    class_name='ReactiveMaterial',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_68390bfb_e307_479d_8f78_d66d8773cb1d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ReactiveMaterial',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    