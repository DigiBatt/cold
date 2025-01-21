
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BariumSaltCompoundModule import BariumSaltCompound







class BariumDifluorooxalatoborate(BariumSaltCompound):
    """
    Class representing the `BariumDifluorooxalatoborate` entity, which inherits from:
    - BariumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_a092c93d_1d03_4d74_b0d7_7ed51b0a3eca'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumDifluorooxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumDifluorooxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_a092c93d_1d03_4d74_b0d7_7ed51b0a3eca',
    
    class_name='BariumDifluorooxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_a092c93d_1d03_4d74_b0d7_7ed51b0a3eca',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumDifluorooxalatoborate',
        alias="class_name"
    )
    

    
    

    

    