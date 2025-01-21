
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SecondGenerationFermionModule import SecondGenerationFermion



from .NeutrinoTypeModule import NeutrinoType







class MuonNeutrino(SecondGenerationFermion, NeutrinoType):
    """
    Class representing the `MuonNeutrino` entity, which inherits from:
    - SecondGenerationFermion, NeutrinoType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_83550665_c68c_4015_86a7_308c9dd2fb4b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MuonNeutrino'`
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
    obj = MuonNeutrino(
    
    class_iri='https://w3id.org/emmo#EMMO_83550665_c68c_4015_86a7_308c9dd2fb4b',
    
    class_name='MuonNeutrino',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_83550665_c68c_4015_86a7_308c9dd2fb4b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MuonNeutrino',
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
    

    
    

    

    