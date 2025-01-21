
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemioticObjectModule import SemioticObject







class Deduced(SemioticObject):
    """
    Class representing the `Deduced` entity, which inherits from:
    - SemioticObject

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_669d2749_bece_460a_b26a_9a909fd8ca4d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Deduced'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Deduced(
    
    class_iri='https://w3id.org/emmo#EMMO_669d2749_bece_460a_b26a_9a909fd8ca4d',
    
    class_name='Deduced',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_669d2749_bece_460a_b26a_9a909fd8ca4d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Deduced',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    