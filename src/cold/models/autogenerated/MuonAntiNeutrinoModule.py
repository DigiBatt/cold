
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SecondGenerationFermionModule import SecondGenerationFermion



from .AntiNeutrinoTypeModule import AntiNeutrinoType







class MuonAntiNeutrino(SecondGenerationFermion, AntiNeutrinoType):
    """
    Class representing the `MuonAntiNeutrino` entity, which inherits from:
    - SecondGenerationFermion, AntiNeutrinoType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2a0f30f5_bb26_4235_9d67_a6b22aca78e3'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MuonAntiNeutrino'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MuonAntiNeutrino(
    
    class_iri='https://w3id.org/emmo#EMMO_2a0f30f5_bb26_4235_9d67_a6b22aca78e3',
    
    class_name='MuonAntiNeutrino',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2a0f30f5_bb26_4235_9d67_a6b22aca78e3',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MuonAntiNeutrino',
        alias="class_name"
    )
    

    
    

    

    