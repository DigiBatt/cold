
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FlowCellModule import FlowCell







class HybridFlowCell(FlowCell):
    """
    Class representing the `HybridFlowCell` entity, which inherits from:
    - FlowCell

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f54474fc_5d07_474b_97ae_f5d0349363b4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'HybridFlowCell'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = HybridFlowCell(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f54474fc_5d07_474b_97ae_f5d0349363b4',
    
    class_name='HybridFlowCell',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f54474fc_5d07_474b_97ae_f5d0349363b4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'HybridFlowCell',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    