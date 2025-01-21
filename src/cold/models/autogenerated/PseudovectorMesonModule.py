
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MesonModule import Meson







class PseudovectorMeson(Meson):
    """
    Class representing the `PseudovectorMeson` entity, which inherits from:
    - Meson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_38d00e5f_d759_4dcc_8551_ab95865cf799'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PseudovectorMeson'`
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
    obj = PseudovectorMeson(
    
    class_iri='https://w3id.org/emmo#EMMO_38d00e5f_d759_4dcc_8551_ab95865cf799',
    
    class_name='PseudovectorMeson',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_38d00e5f_d759_4dcc_8551_ab95865cf799',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PseudovectorMeson',
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
    

    
    

    

    