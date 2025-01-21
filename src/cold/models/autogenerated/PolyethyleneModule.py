
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PolymerCompoundModule import PolymerCompound







class Polyethylene(PolymerCompound):
    """
    Class representing the `Polyethylene` entity, which inherits from:
    - PolymerCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_79220ea3_3426_47a0_9b41_33012d565fc2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Polyethylene'`
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
    obj = Polyethylene(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_79220ea3_3426_47a0_9b41_33012d565fc2',
    
    class_name='Polyethylene',
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_79220ea3_3426_47a0_9b41_33012d565fc2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Polyethylene',
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
    

    
    

    

    