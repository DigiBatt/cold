
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class CadmiumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `CadmiumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_3540fb20_f719_42eb_ad0c_112ffedb7c6d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CadmiumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CadmiumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_3540fb20_f719_42eb_ad0c_112ffedb7c6d',
    
    class_name='CadmiumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_3540fb20_f719_42eb_ad0c_112ffedb7c6d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CadmiumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    