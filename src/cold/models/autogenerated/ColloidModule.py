
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DispersionModule import Dispersion



from .PhaseHeterogeneousMixtureModule import PhaseHeterogeneousMixture







class Colloid(Dispersion, PhaseHeterogeneousMixture):
    """
    Class representing the `Colloid` entity, which inherits from:
    - Dispersion, PhaseHeterogeneousMixture

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_6c487fb3_03d1_4e56_91ed_c2e16dcbef60'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Colloid'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Colloid(
    
    class_iri='https://w3id.org/emmo#EMMO_6c487fb3_03d1_4e56_91ed_c2e16dcbef60',
    
    class_name='Colloid',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_6c487fb3_03d1_4e56_91ed_c2e16dcbef60',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Colloid',
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
    

    
    

    

    