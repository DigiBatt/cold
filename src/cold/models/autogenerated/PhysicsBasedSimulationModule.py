
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SimulationModule import Simulation







class PhysicsBasedSimulation(Simulation):
    """
    Class representing the `PhysicsBasedSimulation` entity, which inherits from:
    - Simulation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e97af6ec_4371_4bbc_8936_34b76e33302f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicsBasedSimulation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicsBasedSimulation(
    
    class_iri='https://w3id.org/emmo#EMMO_e97af6ec_4371_4bbc_8936_34b76e33302f',
    
    class_name='PhysicsBasedSimulation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e97af6ec_4371_4bbc_8936_34b76e33302f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicsBasedSimulation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    