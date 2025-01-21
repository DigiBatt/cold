
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PowerHoldModule import PowerHold







class ConstantPowerDischarging(PowerHold):
    """
    Class representing the `ConstantPowerDischarging` entity, which inherits from:
    - PowerHold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a2f65954_1ed8_4faf_9efe_597018d03e8d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantPowerDischarging'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantPowerDischarging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a2f65954_1ed8_4faf_9efe_597018d03e8d',
    
    class_name='ConstantPowerDischarging',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a2f65954_1ed8_4faf_9efe_597018d03e8d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantPowerDischarging',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    