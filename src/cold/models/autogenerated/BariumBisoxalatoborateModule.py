
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BariumSaltCompoundModule import BariumSaltCompound







class BariumBisoxalatoborate(BariumSaltCompound):
    """
    Class representing the `BariumBisoxalatoborate` entity, which inherits from:
    - BariumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_ad1fe482_6d88_4207_b1e5_ef01b68bec97'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumBisoxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumBisoxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_ad1fe482_6d88_4207_b1e5_ef01b68bec97',
    
    class_name='BariumBisoxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_ad1fe482_6d88_4207_b1e5_ef01b68bec97',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumBisoxalatoborate',
        alias="class_name"
    )
    

    
    

    

    