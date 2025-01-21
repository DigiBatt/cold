
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SimulationApplicationModule import SimulationApplication







class PhysicalBasedSimulationSoftware(SimulationApplication):
    """
    Class representing the `PhysicalBasedSimulationSoftware` entity, which inherits from:
    - SimulationApplication

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8d4962d7_9608_44f7_a2f1_82a4bb173f4a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhysicalBasedSimulationSoftware'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhysicalBasedSimulationSoftware(
    
    class_iri='https://w3id.org/emmo#EMMO_8d4962d7_9608_44f7_a2f1_82a4bb173f4a',
    
    class_name='PhysicalBasedSimulationSoftware',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8d4962d7_9608_44f7_a2f1_82a4bb173f4a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhysicalBasedSimulationSoftware',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    