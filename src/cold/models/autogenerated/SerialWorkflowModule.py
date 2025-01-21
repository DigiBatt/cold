
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkflowModule import Workflow



from .SequenceModule import Sequence







class SerialWorkflow(Workflow, Sequence):
    """
    Class representing the `SerialWorkflow` entity, which inherits from:
    - Workflow, Sequence

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_57ba1bf0_4314_432c_a9bb_6a6720c8dab5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SerialWorkflow'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SerialWorkflow(
    
    class_iri='https://w3id.org/emmo#EMMO_57ba1bf0_4314_432c_a9bb_6a6720c8dab5',
    
    class_name='SerialWorkflow',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_57ba1bf0_4314_432c_a9bb_6a6720c8dab5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SerialWorkflow',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    