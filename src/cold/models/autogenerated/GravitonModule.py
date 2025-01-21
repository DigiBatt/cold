
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalBosonModule import FundamentalBoson







class Graviton(FundamentalBoson):
    """
    Class representing the `Graviton` entity, which inherits from:
    - FundamentalBoson

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_eb3c61f0_3983_4346_a0c6_e7f6b90a67a8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Graviton'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Graviton(
    
    class_iri='https://w3id.org/emmo#EMMO_eb3c61f0_3983_4346_a0c6_e7f6b90a67a8',
    
    class_name='Graviton',
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_eb3c61f0_3983_4346_a0c6_e7f6b90a67a8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Graviton',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    