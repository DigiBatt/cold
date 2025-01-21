
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PolymerCompoundModule import PolymerCompound







class PolyethyleneGlycol(PolymerCompound):
    """
    Class representing the `PolyethyleneGlycol` entity, which inherits from:
    - PolymerCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_dc9ae81a_b5ac_45b6_8b66_9ee6b821d475'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PolyethyleneGlycol'`
        - **Alias**: `class_name`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PolyethyleneGlycol(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_dc9ae81a_b5ac_45b6_8b66_9ee6b821d475',
    
    class_name='PolyethyleneGlycol',
    
    pubChemReference="example_value",
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_dc9ae81a_b5ac_45b6_8b66_9ee6b821d475',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PolyethyleneGlycol',
        alias="class_name"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    