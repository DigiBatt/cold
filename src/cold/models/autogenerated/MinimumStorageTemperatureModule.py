
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MiniumumTemperatureModule import MiniumumTemperature







class MinimumStorageTemperature(MiniumumTemperature):
    """
    Class representing the `MinimumStorageTemperature` entity, which inherits from:
    - MiniumumTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ddfd57a_d338_4690_be45_b26884ed6302'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MinimumStorageTemperature'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MinimumStorageTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ddfd57a_d338_4690_be45_b26884ed6302',
    
    class_name='MinimumStorageTemperature',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ddfd57a_d338_4690_be45_b26884ed6302',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MinimumStorageTemperature',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    