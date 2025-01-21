
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumBisoxalatophosphate(StrontiumSaltCompound):
    """
    Class representing the `StrontiumBisoxalatophosphate` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_c5e6b38b_af73_4664_911b_4a6ecc8f2e3f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumBisoxalatophosphate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumBisoxalatophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_c5e6b38b_af73_4664_911b_4a6ecc8f2e3f',
    
    class_name='StrontiumBisoxalatophosphate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_c5e6b38b_af73_4664_911b_4a6ecc8f2e3f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumBisoxalatophosphate',
        alias="class_name"
    )
    

    
    

    

    