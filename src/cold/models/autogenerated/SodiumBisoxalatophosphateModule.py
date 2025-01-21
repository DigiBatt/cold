
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SodiumSaltCompoundModule import SodiumSaltCompound







class SodiumBisoxalatophosphate(SodiumSaltCompound):
    """
    Class representing the `SodiumBisoxalatophosphate` entity, which inherits from:
    - SodiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0a6ddace_69a9_43af_8cb1_bf1fcfaaea67'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumBisoxalatophosphate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumBisoxalatophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0a6ddace_69a9_43af_8cb1_bf1fcfaaea67',
    
    class_name='SodiumBisoxalatophosphate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0a6ddace_69a9_43af_8cb1_bf1fcfaaea67',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumBisoxalatophosphate',
        alias="class_name"
    )
    

    
    

    

    