
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumTetrafluoroborate(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumTetrafluoroborate` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_c581b064_f357_4378_96bc_dcb2c72013f8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumTetrafluoroborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumTetrafluoroborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_c581b064_f357_4378_96bc_dcb2c72013f8',
    
    class_name='MagnesiumTetrafluoroborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_c581b064_f357_4378_96bc_dcb2c72013f8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumTetrafluoroborate',
        alias="class_name"
    )
    

    
    

    

    