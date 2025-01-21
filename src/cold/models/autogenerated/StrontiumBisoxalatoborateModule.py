
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumBisoxalatoborate(StrontiumSaltCompound):
    """
    Class representing the `StrontiumBisoxalatoborate` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_b5d8ff31_cc34_4f22_bfcc_7ffbe69c0b26'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumBisoxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumBisoxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_b5d8ff31_cc34_4f22_bfcc_7ffbe69c0b26',
    
    class_name='StrontiumBisoxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_b5d8ff31_cc34_4f22_bfcc_7ffbe69c0b26',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumBisoxalatoborate',
        alias="class_name"
    )
    

    
    

    

    