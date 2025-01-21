
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NominalPropertyModule import NominalProperty







class LevelOfExpertise(NominalProperty):
    """
    Class representing the `LevelOfExpertise` entity, which inherits from:
    - NominalProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#LevelOfExpertise'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LevelOfExpertise'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LevelOfExpertise(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#LevelOfExpertise',
    
    class_name='LevelOfExpertise',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#LevelOfExpertise',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LevelOfExpertise',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    