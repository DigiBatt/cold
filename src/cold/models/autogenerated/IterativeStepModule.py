
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkflowModule import Workflow



from .StepModule import Step







class IterativeStep(Workflow, Step):
    """
    Class representing the `IterativeStep` entity, which inherits from:
    - Workflow, Step

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9ac10a20_63d0_4bbd_a5d3_f00a0ad4682c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IterativeStep'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IterativeStep(
    
    class_iri='https://w3id.org/emmo#EMMO_9ac10a20_63d0_4bbd_a5d3_f00a0ad4682c',
    
    class_name='IterativeStep',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9ac10a20_63d0_4bbd_a5d3_f00a0ad4682c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IterativeStep',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    