
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkaliMetalSaltCompoundModule import AlkaliMetalSaltCompound







class LithiumSaltCompound(AlkaliMetalSaltCompound):
    """
    Class representing the `LithiumSaltCompound` entity, which inherits from:
    - AlkaliMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_4744a12c_ca28_46b4_9e59_43c1cc15b536'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_4744a12c_ca28_46b4_9e59_43c1cc15b536',
    
    class_name='LithiumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_4744a12c_ca28_46b4_9e59_43c1cc15b536',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    