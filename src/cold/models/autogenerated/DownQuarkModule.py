
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FirstGenerationFermionModule import FirstGenerationFermion



from .DownQuarkTypeModule import DownQuarkType







class DownQuark(FirstGenerationFermion, DownQuarkType):
    """
    Class representing the `DownQuark` entity, which inherits from:
    - FirstGenerationFermion, DownQuarkType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a4edc1d4_bb38_4897_ba1e_f87e7aa31c5b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DownQuark'`
        - **Alias**: `class_name`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DownQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_a4edc1d4_bb38_4897_ba1e_f87e7aa31c5b',
    
    class_name='DownQuark',
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a4edc1d4_bb38_4897_ba1e_f87e7aa31c5b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DownQuark',
        alias="class_name"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    