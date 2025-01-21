
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SaltModule import Salt







class AmmoniumSaltCompound(Salt):
    """
    Class representing the `AmmoniumSaltCompound` entity, which inherits from:
    - Salt

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_aa92d6c6_2c46_4e7d_9b2c_c95b849041d4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AmmoniumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AmmoniumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_aa92d6c6_2c46_4e7d_9b2c_c95b849041d4',
    
    class_name='AmmoniumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_aa92d6c6_2c46_4e7d_9b2c_c95b849041d4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AmmoniumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    