
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CapacityModule import Capacity







class RatedCapacity(Capacity):
    """
    Class representing the `RatedCapacity` entity, which inherits from:
    - Capacity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9b3b4668_0795_4a35_9965_2af383497a26'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RatedCapacity'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RatedCapacity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9b3b4668_0795_4a35_9965_2af383497a26',
    
    class_name='RatedCapacity',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9b3b4668_0795_4a35_9965_2af383497a26',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RatedCapacity',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    