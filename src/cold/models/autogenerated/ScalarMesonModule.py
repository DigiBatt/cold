
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MesonModule import Meson







class ScalarMeson(Meson):
    """
    Class representing the `ScalarMeson` entity, which inherits from:
    - Meson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3275b6e9_05f1_4912_954f_7d64ac12b2d2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ScalarMeson'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ScalarMeson(
    
    class_iri='https://w3id.org/emmo#EMMO_3275b6e9_05f1_4912_954f_7d64ac12b2d2',
    
    class_name='ScalarMeson',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3275b6e9_05f1_4912_954f_7d64ac12b2d2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ScalarMeson',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    