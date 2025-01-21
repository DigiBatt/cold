
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .LithiumSaltCompoundModule import LithiumSaltCompound







class LithiumTrifluoromethanesulfonyloxalatoborate(LithiumSaltCompound):
    """
    Class representing the `LithiumTrifluoromethanesulfonyloxalatoborate` entity, which inherits from:
    - LithiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_3370cbd2_3fb0_47ba_9a20_50124ae6b4cb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumTrifluoromethanesulfonyloxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumTrifluoromethanesulfonyloxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_3370cbd2_3fb0_47ba_9a20_50124ae6b4cb',
    
    class_name='LithiumTrifluoromethanesulfonyloxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_3370cbd2_3fb0_47ba_9a20_50124ae6b4cb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumTrifluoromethanesulfonyloxalatoborate',
        alias="class_name"
    )
    

    
    

    

    