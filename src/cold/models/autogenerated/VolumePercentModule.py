
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PercentQuantityModule import PercentQuantity







class VolumePercent(PercentQuantity):
    """
    Class representing the `VolumePercent` entity, which inherits from:
    - PercentQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_db37b358_b2f0_4e06_b6ae_8c56c8fbb6ba'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VolumePercent'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VolumePercent(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_db37b358_b2f0_4e06_b6ae_8c56c8fbb6ba',
    
    class_name='VolumePercent',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_db37b358_b2f0_4e06_b6ae_8c56c8fbb6ba',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VolumePercent',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    