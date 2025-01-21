
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ObjectivePropertyModule import ObjectiveProperty







class PulseMagnitude(ObjectiveProperty):
    """
    Class representing the `PulseMagnitude` entity, which inherits from:
    - ObjectiveProperty

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_762ba55f_9b56_4c31_865f_cff2e7d0a94b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PulseMagnitude'`
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
    obj = PulseMagnitude(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_762ba55f_9b56_4c31_865f_cff2e7d0a94b',
    
    class_name='PulseMagnitude',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_762ba55f_9b56_4c31_865f_cff2e7d0a94b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PulseMagnitude',
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
    

    
    

    

    