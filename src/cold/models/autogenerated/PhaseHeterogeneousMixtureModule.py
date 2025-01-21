
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MixtureModule import Mixture







class PhaseHeterogeneousMixture(Mixture):
    """
    Class representing the `PhaseHeterogeneousMixture` entity, which inherits from:
    - Mixture

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0e030040_98a7_49b2_a871_dced1f3a6131'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhaseHeterogeneousMixture'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhaseHeterogeneousMixture(
    
    class_iri='https://w3id.org/emmo#EMMO_0e030040_98a7_49b2_a871_dced1f3a6131',
    
    class_name='PhaseHeterogeneousMixture',
    
    hasProperPart="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0e030040_98a7_49b2_a871_dced1f3a6131',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhaseHeterogeneousMixture',
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
    

    
    

    

    