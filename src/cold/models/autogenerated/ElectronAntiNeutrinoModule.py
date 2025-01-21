
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FirstGenerationFermionModule import FirstGenerationFermion



from .AntiNeutrinoTypeModule import AntiNeutrinoType







class ElectronAntiNeutrino(FirstGenerationFermion, AntiNeutrinoType):
    """
    Class representing the `ElectronAntiNeutrino` entity, which inherits from:
    - FirstGenerationFermion, AntiNeutrinoType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_60d13cae_ea44_4a71_9ca7_ba65f72836a4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectronAntiNeutrino'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectronAntiNeutrino(
    
    class_iri='https://w3id.org/emmo#EMMO_60d13cae_ea44_4a71_9ca7_ba65f72836a4',
    
    class_name='ElectronAntiNeutrino',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_60d13cae_ea44_4a71_9ca7_ba65f72836a4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectronAntiNeutrino',
        alias="class_name"
    )
    

    
    

    

    