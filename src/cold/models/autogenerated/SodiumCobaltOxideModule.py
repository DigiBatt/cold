
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MixedMetalOxideCompoundModule import MixedMetalOxideCompound







class SodiumCobaltOxide(MixedMetalOxideCompound):
    """
    Class representing the `SodiumCobaltOxide` entity, which inherits from:
    - MixedMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_cdd18f0c_e7b3_4d09_b3dd_c09fe4b1adba'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SodiumCobaltOxide'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SodiumCobaltOxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_cdd18f0c_e7b3_4d09_b3dd_c09fe4b1adba',
    
    class_name='SodiumCobaltOxide',
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_cdd18f0c_e7b3_4d09_b3dd_c09fe4b1adba',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SodiumCobaltOxide',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    