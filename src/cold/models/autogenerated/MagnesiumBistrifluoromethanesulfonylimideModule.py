
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumBistrifluoromethanesulfonylimide(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumBistrifluoromethanesulfonylimide` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_62be6033_d836_4fc9_92d4_bd8cf2a9ce3a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumBistrifluoromethanesulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumBistrifluoromethanesulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_62be6033_d836_4fc9_92d4_bd8cf2a9ce3a',
    
    class_name='MagnesiumBistrifluoromethanesulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_62be6033_d836_4fc9_92d4_bd8cf2a9ce3a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumBistrifluoromethanesulfonylimide',
        alias="class_name"
    )
    

    
    

    

    