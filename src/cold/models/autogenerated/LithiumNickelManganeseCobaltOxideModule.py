
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MixedMetalOxideCompoundModule import MixedMetalOxideCompound







class LithiumNickelManganeseCobaltOxide(MixedMetalOxideCompound):
    """
    Class representing the `LithiumNickelManganeseCobaltOxide` entity, which inherits from:
    - MixedMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_3ac62305_acd6_4312_9e31_4f824bd2530d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LithiumNickelManganeseCobaltOxide'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LithiumNickelManganeseCobaltOxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_3ac62305_acd6_4312_9e31_4f824bd2530d',
    
    class_name='LithiumNickelManganeseCobaltOxide',
    
    wikidataReference="example_value",
    
    pubChemReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_3ac62305_acd6_4312_9e31_4f824bd2530d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LithiumNickelManganeseCobaltOxide',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    

    
    

    

    