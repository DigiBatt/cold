
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentLimitModule import CurrentLimit







class MaximumContinuousDischargingCurrent(CurrentLimit):
    """
    Class representing the `MaximumContinuousDischargingCurrent` entity, which inherits from:
    - CurrentLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ba7ac581_0e13_4815_b888_013c378932f5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumContinuousDischargingCurrent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaximumContinuousDischargingCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ba7ac581_0e13_4815_b888_013c378932f5',
    
    class_name='MaximumContinuousDischargingCurrent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ba7ac581_0e13_4815_b888_013c378932f5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumContinuousDischargingCurrent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    