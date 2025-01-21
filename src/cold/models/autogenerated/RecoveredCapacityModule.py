
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatedCapacityModule import RatedCapacity







class RecoveredCapacity(RatedCapacity):
    """
    Class representing the `RecoveredCapacity` entity, which inherits from:
    - RatedCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_73f169de_d189_4d7c_893f_a2549771825c'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RecoveredCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RecoveredCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_73f169de_d189_4d7c_893f_a2549771825c',
    
    class_name='RecoveredCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_73f169de_d189_4d7c_893f_a2549771825c',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RecoveredCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    