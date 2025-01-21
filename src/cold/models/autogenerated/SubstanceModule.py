
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CompositePhysicalObjectModule import CompositePhysicalObject



from .MatterModule import Matter







class Substance(CompositePhysicalObject, Matter):
    """
    Class representing the `Substance` entity, which inherits from:
    - CompositePhysicalObject, Matter

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_bc37743c_37c4_4ec7_9d58_d1aae5567352'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Substance'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Substance(
    
    class_iri='https://w3id.org/emmo#EMMO_bc37743c_37c4_4ec7_9d58_d1aae5567352',
    
    class_name='Substance',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_bc37743c_37c4_4ec7_9d58_d1aae5567352',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Substance',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    