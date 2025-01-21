
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompositeFermionModule import CompositeFermion



from .HadronModule import Hadron







class Baryon(CompositeFermion, Hadron):
    """
    Class representing the `Baryon` entity, which inherits from:
    - CompositeFermion, Hadron

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_24dda193_ada8_433b_bb74_6ca4a0b89a20'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Baryon'`
        - **Alias**: `class_name`
    
    - `hasProperPart` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasProperPart`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Baryon(
    
    class_iri='https://w3id.org/emmo#EMMO_24dda193_ada8_433b_bb74_6ca4a0b89a20',
    
    class_name='Baryon',
    
    hasProperPart="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_24dda193_ada8_433b_bb74_6ca4a0b89a20',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Baryon',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    