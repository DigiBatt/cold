
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialModule import Material







class ChemicallyDefinedMaterial(Material):
    """
    Class representing the `ChemicallyDefinedMaterial` entity, which inherits from:
    - Material

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a96e2152_40e7_409c_a53a_fdb9f141eb6a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicallyDefinedMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChemicallyDefinedMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_a96e2152_40e7_409c_a53a_fdb9f141eb6a',
    
    class_name='ChemicallyDefinedMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a96e2152_40e7_409c_a53a_fdb9f141eb6a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicallyDefinedMaterial',
        alias="class_name"
    )
    

    
    

    

    