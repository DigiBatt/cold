
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FirstGenerationFermionModule import FirstGenerationFermion



from .NeutrinoTypeModule import NeutrinoType







class ElectronNeutrino(FirstGenerationFermion, NeutrinoType):
    """
    Class representing the `ElectronNeutrino` entity, which inherits from:
    - FirstGenerationFermion, NeutrinoType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1d5305d7_5690_4e5a_92de_4611e8c356ef'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectronNeutrino'`
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
    obj = ElectronNeutrino(
    
    class_iri='https://w3id.org/emmo#EMMO_1d5305d7_5690_4e5a_92de_4611e8c356ef',
    
    class_name='ElectronNeutrino',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1d5305d7_5690_4e5a_92de_4611e8c356ef',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectronNeutrino',
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
    

    
    

    

    