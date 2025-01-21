
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalSaltCompoundModule import TransitionMetalSaltCompound







class IronSalt(TransitionMetalSaltCompound):
    """
    Class representing the `IronSalt` entity, which inherits from:
    - TransitionMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_4154e6b6_8e3c_4173_91aa_e8ba403bde85'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IronSalt'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IronSalt(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_4154e6b6_8e3c_4173_91aa_e8ba403bde85',
    
    class_name='IronSalt',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_4154e6b6_8e3c_4173_91aa_e8ba403bde85',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IronSalt',
        alias="class_name"
    )
    

    
    

    

    