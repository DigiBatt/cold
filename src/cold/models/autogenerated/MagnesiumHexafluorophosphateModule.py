
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumHexafluorophosphate(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumHexafluorophosphate` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_00db9ba1_7259_4180_a82e_7ed4dafc29a9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumHexafluorophosphate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumHexafluorophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_00db9ba1_7259_4180_a82e_7ed4dafc29a9',
    
    class_name='MagnesiumHexafluorophosphate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_00db9ba1_7259_4180_a82e_7ed4dafc29a9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumHexafluorophosphate',
        alias="class_name"
    )
    

    
    

    

    