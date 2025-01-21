
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PostTransitionMetalSaltCompoundModule import PostTransitionMetalSaltCompound







class AluminiumSaltCompound(PostTransitionMetalSaltCompound):
    """
    Class representing the `AluminiumSaltCompound` entity, which inherits from:
    - PostTransitionMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_f313522b_e2c4_4251_ba7f_d6b9dc7db1d6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AluminiumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AluminiumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_f313522b_e2c4_4251_ba7f_d6b9dc7db1d6',
    
    class_name='AluminiumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_f313522b_e2c4_4251_ba7f_d6b9dc7db1d6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AluminiumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    