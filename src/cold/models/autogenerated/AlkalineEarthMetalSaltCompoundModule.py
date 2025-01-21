
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SaltModule import Salt







class AlkalineEarthMetalSaltCompound(Salt):
    """
    Class representing the `AlkalineEarthMetalSaltCompound` entity, which inherits from:
    - Salt

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_fc93282d_cb35_4bab_81a8_78689ae59e5f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkalineEarthMetalSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlkalineEarthMetalSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_fc93282d_cb35_4bab_81a8_78689ae59e5f',
    
    class_name='AlkalineEarthMetalSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_fc93282d_cb35_4bab_81a8_78689ae59e5f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkalineEarthMetalSaltCompound',
        alias="class_name"
    )
    

    
    

    

    