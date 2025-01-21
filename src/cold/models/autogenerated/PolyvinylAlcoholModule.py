
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PolymerCompoundModule import PolymerCompound



from .AlcoholModule import Alcohol







class PolyvinylAlcohol(PolymerCompound, Alcohol):
    """
    Class representing the `PolyvinylAlcohol` entity, which inherits from:
    - PolymerCompound, Alcohol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_8f867fdb_27b7_4d6f_9628_98da5afcad5b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PolyvinylAlcohol'`
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
    obj = PolyvinylAlcohol(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_8f867fdb_27b7_4d6f_9628_98da5afcad5b',
    
    class_name='PolyvinylAlcohol',
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_8f867fdb_27b7_4d6f_9628_98da5afcad5b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PolyvinylAlcohol',
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
    

    
    

    

    