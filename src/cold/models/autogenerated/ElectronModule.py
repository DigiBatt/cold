
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FirstGenerationFermionModule import FirstGenerationFermion



from .ElectronTypeModule import ElectronType







class Electron(FirstGenerationFermion, ElectronType):
    """
    Class representing the `Electron` entity, which inherits from:
    - FirstGenerationFermion, ElectronType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8043d3c6_a4c1_4089_ba34_9744e28e5b3d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electron'`
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
    obj = Electron(
    
    class_iri='https://w3id.org/emmo#EMMO_8043d3c6_a4c1_4089_ba34_9744e28e5b3d',
    
    class_name='Electron',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8043d3c6_a4c1_4089_ba34_9744e28e5b3d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electron',
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
    

    
    

    

    