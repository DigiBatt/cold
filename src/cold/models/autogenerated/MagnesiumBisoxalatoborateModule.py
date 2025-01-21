
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagnesiumSaltCompoundModule import MagnesiumSaltCompound







class MagnesiumBisoxalatoborate(MagnesiumSaltCompound):
    """
    Class representing the `MagnesiumBisoxalatoborate` entity, which inherits from:
    - MagnesiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_27696fcd_aa90_44b9_816a_c19400f0ab9a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MagnesiumBisoxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MagnesiumBisoxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_27696fcd_aa90_44b9_816a_c19400f0ab9a',
    
    class_name='MagnesiumBisoxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_27696fcd_aa90_44b9_816a_c19400f0ab9a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MagnesiumBisoxalatoborate',
        alias="class_name"
    )
    

    
    

    

    