
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IronOxideCompoundModule import IronOxideCompound







class IronIIIOxide(IronOxideCompound):
    """
    Class representing the `IronIIIOxide` entity, which inherits from:
    - IronOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_383f6ea4_344d_4f3f_ae04_4c5005e9c8fd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IronIIIOxide'`
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
    obj = IronIIIOxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_383f6ea4_344d_4f3f_ae04_4c5005e9c8fd',
    
    class_name='IronIIIOxide',
    
    pubChemReference="example_value",
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_383f6ea4_344d_4f3f_ae04_4c5005e9c8fd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IronIIIOxide',
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
    

    
    

    

    