
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FirstGenerationFermionModule import FirstGenerationFermion



from .UpQuarkTypeModule import UpQuarkType







class UpQuark(FirstGenerationFermion, UpQuarkType):
    """
    Class representing the `UpQuark` entity, which inherits from:
    - FirstGenerationFermion, UpQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0a3f04a6_ba3a_49d9_99da_08b0e26f51f0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'UpQuark'`
        - **Alias**: `class_name`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = UpQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_0a3f04a6_ba3a_49d9_99da_08b0e26f51f0',
    
    class_name='UpQuark',
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0a3f04a6_ba3a_49d9_99da_08b0e26f51f0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'UpQuark',
        alias="class_name"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    