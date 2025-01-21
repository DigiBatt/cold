
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EstimationModule import Estimation







class Assignment(Estimation):
    """
    Class representing the `Assignment` entity, which inherits from:
    - Estimation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d5adc819_d4b2_4661_b429_1705b75d5053'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Assignment'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Assignment(
    
    class_iri='https://w3id.org/emmo#EMMO_d5adc819_d4b2_4661_b429_1705b75d5053',
    
    class_name='Assignment',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d5adc819_d4b2_4661_b429_1705b75d5053',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Assignment',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    