
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaximumTemperatureModule import MaximumTemperature







class MaximumStorageTemperature(MaximumTemperature):
    """
    Class representing the `MaximumStorageTemperature` entity, which inherits from:
    - MaximumTemperature

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ea4d188_9701_4699_a5ca_812a98a9afa7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MaximumStorageTemperature'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MaximumStorageTemperature(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ea4d188_9701_4699_a5ca_812a98a9afa7',
    
    class_name='MaximumStorageTemperature',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0ea4d188_9701_4699_a5ca_812a98a9afa7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MaximumStorageTemperature',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    