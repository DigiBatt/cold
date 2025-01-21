
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MixedMetalOxideCompoundModule import MixedMetalOxideCompound







class LithiumNickelCobaltAluminiumOxide(MixedMetalOxideCompound):
    """
    Class representing the `LithiumNickelCobaltAluminiumOxide` entity, which inherits from:
    - MixedMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_cd17ca33_ae3d_4738_8930_547673bf6c1f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumNickelCobaltAluminiumOxide'`
        - **Alias**: `class_name`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumNickelCobaltAluminiumOxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_cd17ca33_ae3d_4738_8930_547673bf6c1f',
    
    class_name='LithiumNickelCobaltAluminiumOxide',
    
    pubChemReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_cd17ca33_ae3d_4738_8930_547673bf6c1f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumNickelCobaltAluminiumOxide',
        alias="class_name"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    

    
    

    

    