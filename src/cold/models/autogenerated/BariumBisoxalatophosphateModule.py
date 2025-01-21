
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BariumSaltCompoundModule import BariumSaltCompound







class BariumBisoxalatophosphate(BariumSaltCompound):
    """
    Class representing the `BariumBisoxalatophosphate` entity, which inherits from:
    - BariumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_55d2a257_feb3_4af1_bf8d_4b53bb73610c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumBisoxalatophosphate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumBisoxalatophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_55d2a257_feb3_4af1_bf8d_4b53bb73610c',
    
    class_name='BariumBisoxalatophosphate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_55d2a257_feb3_4af1_bf8d_4b53bb73610c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumBisoxalatophosphate',
        alias="class_name"
    )
    

    
    

    

    