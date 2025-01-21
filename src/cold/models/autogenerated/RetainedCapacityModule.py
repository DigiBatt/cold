
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RatedCapacityModule import RatedCapacity







class RetainedCapacity(RatedCapacity):
    """
    Class representing the `RetainedCapacity` entity, which inherits from:
    - RatedCapacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b8d4042d_329a_450f_9088_2fc0e16a8667'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RetainedCapacity'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RetainedCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b8d4042d_329a_450f_9088_2fc0e16a8667',
    
    class_name='RetainedCapacity',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b8d4042d_329a_450f_9088_2fc0e16a8667',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RetainedCapacity',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    