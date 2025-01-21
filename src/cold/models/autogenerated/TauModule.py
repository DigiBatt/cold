
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ThirdGenerationFermionModule import ThirdGenerationFermion



from .ElectronTypeModule import ElectronType







class Tau(ThirdGenerationFermion, ElectronType):
    """
    Class representing the `Tau` entity, which inherits from:
    - ThirdGenerationFermion, ElectronType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3a948fa6_033a_4bb2_a319_36a45741d832'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Tau'`
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
    obj = Tau(
    
    class_iri='https://w3id.org/emmo#EMMO_3a948fa6_033a_4bb2_a319_36a45741d832',
    
    class_name='Tau',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3a948fa6_033a_4bb2_a319_36a45741d832',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Tau',
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
    

    
    

    

    