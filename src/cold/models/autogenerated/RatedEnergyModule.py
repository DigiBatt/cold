
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StoredEnergyModule import StoredEnergy







class RatedEnergy(StoredEnergy):
    """
    Class representing the `RatedEnergy` entity, which inherits from:
    - StoredEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_da215d1a_196a_465f_9de8_89f6fbb76982'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RatedEnergy'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RatedEnergy(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_da215d1a_196a_465f_9de8_89f6fbb76982',
    
    class_name='RatedEnergy',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_da215d1a_196a_465f_9de8_89f6fbb76982',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RatedEnergy',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    