
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThirdGenerationFermionModule import ThirdGenerationFermion



from .NeutrinoTypeModule import NeutrinoType







class TauNeutrino(ThirdGenerationFermion, NeutrinoType):
    """
    Class representing the `TauNeutrino` entity, which inherits from:
    - ThirdGenerationFermion, NeutrinoType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_eb95a619_ca07_4678_a809_10021b25a13f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TauNeutrino'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TauNeutrino(
    
    class_iri='https://w3id.org/emmo#EMMO_eb95a619_ca07_4678_a809_10021b25a13f',
    
    class_name='TauNeutrino',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_eb95a619_ca07_4678_a809_10021b25a13f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TauNeutrino',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    