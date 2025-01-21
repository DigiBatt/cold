
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicsBasedSimulationModule import PhysicsBasedSimulation







class StandaloneModelSimulation(PhysicsBasedSimulation):
    """
    Class representing the `StandaloneModelSimulation` entity, which inherits from:
    - PhysicsBasedSimulation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d0bcf2ca_cd55_4f34_8fc2_2decc4c6087a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandaloneModelSimulation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StandaloneModelSimulation(
    
    class_iri='https://w3id.org/emmo#EMMO_d0bcf2ca_cd55_4f34_8fc2_2decc4c6087a',
    
    class_name='StandaloneModelSimulation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d0bcf2ca_cd55_4f34_8fc2_2decc4c6087a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandaloneModelSimulation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    