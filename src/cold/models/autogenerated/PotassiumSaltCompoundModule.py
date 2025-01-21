
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkaliMetalSaltCompoundModule import AlkaliMetalSaltCompound







class PotassiumSaltCompound(AlkaliMetalSaltCompound):
    """
    Class representing the `PotassiumSaltCompound` entity, which inherits from:
    - AlkaliMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_c6e80ad7_1aef_4c6d_a51a_4aec8855a68f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PotassiumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PotassiumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_c6e80ad7_1aef_4c6d_a51a_4aec8855a68f',
    
    class_name='PotassiumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_c6e80ad7_1aef_4c6d_a51a_4aec8855a68f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PotassiumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    