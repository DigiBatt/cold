
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ResourceIdentifierModule import ResourceIdentifier



from .CausalSystemModule import CausalSystem







class IRI(ResourceIdentifier, CausalSystem):
    """
    Class representing the `IRI` entity, which inherits from:
    - ResourceIdentifier, CausalSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5c15f8c4_d2de_47a0_acdd_470b8dda979b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IRI'`
        - **Alias**: `class_name`
    
    - `hasSpatialSlice` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialSlice`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IRI(
    
    class_iri='https://w3id.org/emmo#EMMO_5c15f8c4_d2de_47a0_acdd_470b8dda979b',
    
    class_name='IRI',
    
    hasSpatialSlice="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5c15f8c4_d2de_47a0_acdd_470b8dda979b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IRI',
        alias="class_name"
    )
    
    hasSpatialSlice: Optional[str] = Field(
        None,
        alias="hasSpatialSlice"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    