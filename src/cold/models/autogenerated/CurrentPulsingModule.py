
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CurrentControlledProcessModule import CurrentControlledProcess







class CurrentPulsing(CurrentControlledProcess):
    """
    Class representing the `CurrentPulsing` entity, which inherits from:
    - CurrentControlledProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9f1ffb54_4403_4541_98c1_3a821c6d060f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CurrentPulsing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CurrentPulsing(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9f1ffb54_4403_4541_98c1_3a821c6d060f',
    
    class_name='CurrentPulsing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_9f1ffb54_4403_4541_98c1_3a821c6d060f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CurrentPulsing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    