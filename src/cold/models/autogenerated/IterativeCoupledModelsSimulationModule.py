
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoupledModule import Coupled







class IterativeCoupledModelsSimulation(Coupled):
    """
    Class representing the `IterativeCoupledModelsSimulation` entity, which inherits from:
    - Coupled

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_01354ac2_cce1_4b7d_8b4a_7322d6cb10bc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IterativeCoupledModelsSimulation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IterativeCoupledModelsSimulation(
    
    class_iri='https://w3id.org/emmo#EMMO_01354ac2_cce1_4b7d_8b4a_7322d6cb10bc',
    
    class_name='IterativeCoupledModelsSimulation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_01354ac2_cce1_4b7d_8b4a_7322d6cb10bc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IterativeCoupledModelsSimulation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    