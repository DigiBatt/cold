
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumBisoxalatophosphate(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumBisoxalatophosphate` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_c0ed3eca_64ef_4e69_a415_3e5f76ca27b6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumBisoxalatophosphate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumBisoxalatophosphate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_c0ed3eca_64ef_4e69_a415_3e5f76ca27b6',
    
    class_name='MagnesiumBisoxalatophosphate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_c0ed3eca_64ef_4e69_a415_3e5f76ca27b6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumBisoxalatophosphate',
        alias="class_name"
    )
    

    
    

    

    