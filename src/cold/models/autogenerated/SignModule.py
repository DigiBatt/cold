
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SemioticEntityModule import SemioticEntity







class Sign(SemioticEntity):
    """
    Class representing the `Sign` entity, which inherits from:
    - SemioticEntity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b21a56ed_f969_4612_a6ec_cb7766f7f31d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Sign'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Sign(
    
    class_iri='https://w3id.org/emmo#EMMO_b21a56ed_f969_4612_a6ec_cb7766f7f31d',
    
    class_name='Sign',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b21a56ed_f969_4612_a6ec_cb7766f7f31d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Sign',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    