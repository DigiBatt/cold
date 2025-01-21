
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineEarthMetalSaltCompoundModule import AlkalineEarthMetalSaltCompound







class StrontiumSaltCompound(AlkalineEarthMetalSaltCompound):
    """
    Class representing the `StrontiumSaltCompound` entity, which inherits from:
    - AlkalineEarthMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_a06bf8d8_24d5_4b29_a633_e5c00b1bd746'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_a06bf8d8_24d5_4b29_a633_e5c00b1bd746',
    
    class_name='StrontiumSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_a06bf8d8_24d5_4b29_a633_e5c00b1bd746',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumSaltCompound',
        alias="class_name"
    )
    

    
    

    

    