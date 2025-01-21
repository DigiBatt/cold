
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentLimitModule import CurrentLimit







class MaximumContinuousChargingCurrent(CurrentLimit):
    """
    Class representing the `MaximumContinuousChargingCurrent` entity, which inherits from:
    - CurrentLimit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_39d8a6ee_cd55_4855_8b5b_d42bef95ac78'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumContinuousChargingCurrent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaximumContinuousChargingCurrent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_39d8a6ee_cd55_4855_8b5b_d42bef95ac78',
    
    class_name='MaximumContinuousChargingCurrent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_39d8a6ee_cd55_4855_8b5b_d42bef95ac78',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumContinuousChargingCurrent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    