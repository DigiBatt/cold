
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MolecularEntityModule import MolecularEntity







class Atom(MolecularEntity):
    """
    Class representing the `Atom` entity, which inherits from:
    - MolecularEntity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_eb77076b_a104_42ac_a065_798b2d2809ad'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Atom'`
        - **Alias**: `class_name`
    
    - `hasSpatialSlice` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialSlice`
    
    - `hasSpatialPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSpatialPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Atom(
    
    class_iri='https://w3id.org/emmo#EMMO_eb77076b_a104_42ac_a065_798b2d2809ad',
    
    class_name='Atom',
    
    hasSpatialSlice="example_value",
    
    hasSpatialPart="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_eb77076b_a104_42ac_a065_798b2d2809ad',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Atom',
        alias="class_name"
    )
    
    hasSpatialSlice: Optional[str] = Field(
        None,
        alias="hasSpatialSlice"
    )
    
    hasSpatialPart: Optional[str] = Field(
        None,
        alias="hasSpatialPart"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    