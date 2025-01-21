
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .HybridMatterModule import HybridMatter



from .CompositeBosonModule import CompositeBoson



from .HadronModule import Hadron







class Meson(HybridMatter, CompositeBoson, Hadron):
    """
    Class representing the `Meson` entity, which inherits from:
    - HybridMatter, CompositeBoson, Hadron

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_be0a7278_b4e6_4bca_88ba_de3f67a478e2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Meson'`
        - **Alias**: `class_name`
    
    - `hasProperPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasProperPart`
    
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
    obj = Meson(
    
    class_iri='https://w3id.org/emmo#EMMO_be0a7278_b4e6_4bca_88ba_de3f67a478e2',
    
    class_name='Meson',
    
    hasProperPart="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_be0a7278_b4e6_4bca_88ba_de3f67a478e2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Meson',
        alias="class_name"
    )
    
    hasProperPart: Optional[str] = Field(
        None,
        alias="hasProperPart"
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
    

    
    

    

    