
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SaltModule import Salt







class ZincSaltCompound(Salt):
    """
    Class representing the `ZincSaltCompound` entity, which inherits from:
    - Salt

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_b07a5287_67d1_4f4f_9640_e0146f713a6c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_b07a5287_67d1_4f4f_9640_e0146f713a6c',
    
    class_name='ZincSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_b07a5287_67d1_4f4f_9640_e0146f713a6c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincSaltCompound',
        alias="class_name"
    )
    

    
    

    

    