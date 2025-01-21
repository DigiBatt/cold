
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PowerHoldModule import PowerHold







class ConstantPowerCharging(PowerHold):
    """
    Class representing the `ConstantPowerCharging` entity, which inherits from:
    - PowerHold

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dcd4a15d_52cf_44fb_b826_df18e4baa89c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ConstantPowerCharging'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ConstantPowerCharging(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dcd4a15d_52cf_44fb_b826_df18e4baa89c',
    
    class_name='ConstantPowerCharging',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dcd4a15d_52cf_44fb_b826_df18e4baa89c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ConstantPowerCharging',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    