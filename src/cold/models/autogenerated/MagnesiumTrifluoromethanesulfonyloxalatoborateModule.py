
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumTrifluoromethanesulfonyloxalatoborate(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumTrifluoromethanesulfonyloxalatoborate` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_2b7473ba_9156_489a_880f_3a2f746cd104'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumTrifluoromethanesulfonyloxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumTrifluoromethanesulfonyloxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_2b7473ba_9156_489a_880f_3a2f746cd104',
    
    class_name='MagnesiumTrifluoromethanesulfonyloxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_2b7473ba_9156_489a_880f_3a2f746cd104',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumTrifluoromethanesulfonyloxalatoborate',
        alias="class_name"
    )
    

    
    

    

    