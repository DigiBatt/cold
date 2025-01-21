
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PerspectiveModule import Perspective







class Perceptual(Perspective):
    """
    Class representing the `Perceptual` entity, which inherits from:
    - Perspective

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_649bf97b_4397_4005_90d9_219755d92e34'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Perceptual'`
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
    obj = Perceptual(
    
    class_iri='https://w3id.org/emmo#EMMO_649bf97b_4397_4005_90d9_219755d92e34',
    
    class_name='Perceptual',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_649bf97b_4397_4005_90d9_219755d92e34',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Perceptual',
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
    

    
    

    

    