
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysicsBasedSimulationModule import PhysicsBasedSimulation







class MultiSimulation(PhysicsBasedSimulation):
    """
    Class representing the `MultiSimulation` entity, which inherits from:
    - PhysicsBasedSimulation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_7d56ec24_499d_487a_af7d_a91aaa787bfe'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MultiSimulation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MultiSimulation(
    
    class_iri='https://w3id.org/emmo#EMMO_7d56ec24_499d_487a_af7d_a91aaa787bfe',
    
    class_name='MultiSimulation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_7d56ec24_499d_487a_af7d_a91aaa787bfe',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MultiSimulation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    