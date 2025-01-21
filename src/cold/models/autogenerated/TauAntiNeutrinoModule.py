
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThirdGenerationFermionModule import ThirdGenerationFermion



from .AntiNeutrinoTypeModule import AntiNeutrinoType







class TauAntiNeutrino(ThirdGenerationFermion, AntiNeutrinoType):
    """
    Class representing the `TauAntiNeutrino` entity, which inherits from:
    - ThirdGenerationFermion, AntiNeutrinoType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_de5e558c_2066_4b1f_b888_e2503bcafee0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TauAntiNeutrino'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TauAntiNeutrino(
    
    class_iri='https://w3id.org/emmo#EMMO_de5e558c_2066_4b1f_b888_e2503bcafee0',
    
    class_name='TauAntiNeutrino',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_de5e558c_2066_4b1f_b888_e2503bcafee0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TauAntiNeutrino',
        alias="class_name"
    )
    

    
    

    

    