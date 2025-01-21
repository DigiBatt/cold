
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumBisfluorosulfonylimide(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumBisfluorosulfonylimide` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_43ec3168_0f1a_44aa_99ad_716fcc48bbcb'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumBisfluorosulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumBisfluorosulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_43ec3168_0f1a_44aa_99ad_716fcc48bbcb',
    
    class_name='MagnesiumBisfluorosulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_43ec3168_0f1a_44aa_99ad_716fcc48bbcb',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumBisfluorosulfonylimide',
        alias="class_name"
    )
    

    
    

    

    