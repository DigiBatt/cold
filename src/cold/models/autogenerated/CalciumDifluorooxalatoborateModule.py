
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CalciumSaltCompoundModule import CalciumSaltCompound







class CalciumDifluorooxalatoborate(CalciumSaltCompound):
    """
    Class representing the `CalciumDifluorooxalatoborate` entity, which inherits from:
    - CalciumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_55b09b6b_c8cd_410c_8971_b2bd86e0c905'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CalciumDifluorooxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CalciumDifluorooxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_55b09b6b_c8cd_410c_8971_b2bd86e0c905',
    
    class_name='CalciumDifluorooxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_55b09b6b_c8cd_410c_8971_b2bd86e0c905',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CalciumDifluorooxalatoborate',
        alias="class_name"
    )
    

    
    

    

    