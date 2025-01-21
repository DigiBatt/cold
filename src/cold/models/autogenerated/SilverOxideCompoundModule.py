
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class SilverOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `SilverOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_f24cfd50_5d01_4e02_88b5_44a609cfa432'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SilverOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SilverOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_f24cfd50_5d01_4e02_88b5_44a609cfa432',
    
    class_name='SilverOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_f24cfd50_5d01_4e02_88b5_44a609cfa432',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SilverOxideCompound',
        alias="class_name"
    )
    

    
    

    

    