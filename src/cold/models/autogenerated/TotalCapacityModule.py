
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CapacityModule import Capacity







class TotalCapacity(Capacity):
    """
    Class representing the `TotalCapacity` entity, which inherits from:
    - Capacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_df9e9d49_12fa_4794_b482_e0dcd2a7bb66'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TotalCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TotalCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_df9e9d49_12fa_4794_b482_e0dcd2a7bb66',
    
    class_name='TotalCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_df9e9d49_12fa_4794_b482_e0dcd2a7bb66',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TotalCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    