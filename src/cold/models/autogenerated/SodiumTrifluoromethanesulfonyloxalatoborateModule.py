
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SodiumSaltCompoundModule import SodiumSaltCompound







class SodiumTrifluoromethanesulfonyloxalatoborate(SodiumSaltCompound):
    """
    Class representing the `SodiumTrifluoromethanesulfonyloxalatoborate` entity, which inherits from:
    - SodiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_1be34841_81f7_4216_8290_6bd75361a1c9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumTrifluoromethanesulfonyloxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumTrifluoromethanesulfonyloxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_1be34841_81f7_4216_8290_6bd75361a1c9',
    
    class_name='SodiumTrifluoromethanesulfonyloxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_1be34841_81f7_4216_8290_6bd75361a1c9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumTrifluoromethanesulfonyloxalatoborate',
        alias="class_name"
    )
    

    
    

    

    