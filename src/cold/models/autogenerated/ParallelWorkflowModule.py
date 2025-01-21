
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkflowModule import Workflow







class ParallelWorkflow(Workflow):
    """
    Class representing the `ParallelWorkflow` entity, which inherits from:
    - Workflow

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_5848e476_2768_4988_98f9_9053c532307b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ParallelWorkflow'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ParallelWorkflow(
    
    class_iri='https://w3id.org/emmo#EMMO_5848e476_2768_4988_98f9_9053c532307b',
    
    class_name='ParallelWorkflow',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_5848e476_2768_4988_98f9_9053c532307b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ParallelWorkflow',
        alias="class_name"
    )
    

    
    

    

    