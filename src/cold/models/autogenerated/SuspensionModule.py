
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DispersionModule import Dispersion



from .PhaseHeterogeneousMixtureModule import PhaseHeterogeneousMixture



from .StateOfMatterModule import StateOfMatter







class Suspension(Dispersion, PhaseHeterogeneousMixture, StateOfMatter):
    """
    Class representing the `Suspension` entity, which inherits from:
    - Dispersion, PhaseHeterogeneousMixture, StateOfMatter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4a464c8d_8895_44a8_a628_aed13509f1bd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Suspension'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Suspension(
    
    class_iri='https://w3id.org/emmo#EMMO_4a464c8d_8895_44a8_a628_aed13509f1bd',
    
    class_name='Suspension',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4a464c8d_8895_44a8_a628_aed13509f1bd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Suspension',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    