
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SaltModule import Salt







class TransitionMetalSaltCompound(Salt):
    """
    Class representing the `TransitionMetalSaltCompound` entity, which inherits from:
    - Salt

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_015116fe_94ca_4be5_9d14_9d9457a47a72'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransitionMetalSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TransitionMetalSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_015116fe_94ca_4be5_9d14_9d9457a47a72',
    
    class_name='TransitionMetalSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_015116fe_94ca_4be5_9d14_9d9457a47a72',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransitionMetalSaltCompound',
        alias="class_name"
    )
    

    
    

    

    