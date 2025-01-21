
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ConventionalModule import Conventional







class Uncoded(Conventional):
    """
    Class representing the `Uncoded` entity, which inherits from:
    - Conventional

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6e78433a_dbb9_409a_a7c0_4037f79d4ed8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Uncoded'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Uncoded(
    
    class_iri='https://w3id.org/emmo#EMMO_6e78433a_dbb9_409a_a7c0_4037f79d4ed8',
    
    class_name='Uncoded',
    
    example="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6e78433a_dbb9_409a_a7c0_4037f79d4ed8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Uncoded',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    