
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PercentQuantityModule import PercentQuantity







class WeightPercent(PercentQuantity):
    """
    Class representing the `WeightPercent` entity, which inherits from:
    - PercentQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2c0e66c8_d58d_44b2_b0ce_ba55194bd505'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WeightPercent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WeightPercent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2c0e66c8_d58d_44b2_b0ce_ba55194bd505',
    
    class_name='WeightPercent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_2c0e66c8_d58d_44b2_b0ce_ba55194bd505',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WeightPercent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    