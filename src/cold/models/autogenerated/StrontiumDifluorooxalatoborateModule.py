
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumDifluorooxalatoborate(StrontiumSaltCompound):
    """
    Class representing the `StrontiumDifluorooxalatoborate` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_6ce8569b_1367_4afd_954b_10eaccb8167c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumDifluorooxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumDifluorooxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_6ce8569b_1367_4afd_954b_10eaccb8167c',
    
    class_name='StrontiumDifluorooxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_6ce8569b_1367_4afd_954b_10eaccb8167c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumDifluorooxalatoborate',
        alias="class_name"
    )
    

    
    

    

    