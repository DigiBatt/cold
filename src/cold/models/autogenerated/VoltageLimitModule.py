
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VoltageModule import Voltage



from .LimitQuantityModule import LimitQuantity







class VoltageLimit(Voltage, LimitQuantity):
    """
    Class representing the `VoltageLimit` entity, which inherits from:
    - Voltage, LimitQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5ebeea80_af22_456b_9087_78c2a8465c58'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VoltageLimit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VoltageLimit(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5ebeea80_af22_456b_9087_78c2a8465c58',
    
    class_name='VoltageLimit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_5ebeea80_af22_456b_9087_78c2a8465c58',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VoltageLimit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    