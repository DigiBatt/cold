
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SodiumSaltCompoundModule import SodiumSaltCompound







class SodiumBisoxalatoborate(SodiumSaltCompound):
    """
    Class representing the `SodiumBisoxalatoborate` entity, which inherits from:
    - SodiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_e884ea99_9b69_4b8e_b932_9c47e1c8ce0c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumBisoxalatoborate'`
        - **Alias**: `class_name`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumBisoxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_e884ea99_9b69_4b8e_b932_9c47e1c8ce0c',
    
    class_name='SodiumBisoxalatoborate',
    
    pubChemReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_e884ea99_9b69_4b8e_b932_9c47e1c8ce0c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumBisoxalatoborate',
        alias="class_name"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    

    
    

    

    