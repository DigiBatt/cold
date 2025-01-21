
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StepModule import Step



from .ThroughTileModule import ThroughTile







class InternalStep(Step, ThroughTile):
    """
    Class representing the `InternalStep` entity, which inherits from:
    - Step, ThroughTile

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_322ce14e_9ede_4841_ad70_302b4d6c5f28'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InternalStep'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InternalStep(
    
    class_iri='https://w3id.org/emmo#EMMO_322ce14e_9ede_4841_ad70_302b4d6c5f28',
    
    class_name='InternalStep',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_322ce14e_9ede_4841_ad70_302b4d6c5f28',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InternalStep',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    