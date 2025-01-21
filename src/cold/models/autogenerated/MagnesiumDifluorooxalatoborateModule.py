
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumDifluorooxalatoborate(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumDifluorooxalatoborate` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_82d57014_0870_45f3_ab05_0f97c05b531d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumDifluorooxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumDifluorooxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_82d57014_0870_45f3_ab05_0f97c05b531d',
    
    class_name='MagnesiumDifluorooxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_82d57014_0870_45f3_ab05_0f97c05b531d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumDifluorooxalatoborate',
        alias="class_name"
    )
    

    
    

    

    