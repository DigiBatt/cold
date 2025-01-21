
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MaterialRelationModule import MaterialRelation







class ElectrochemicalRelation(MaterialRelation):
    """
    Class representing the `ElectrochemicalRelation` entity, which inherits from:
    - MaterialRelation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3d805c2a_4801_440e_9e4d_0fa5585c76ae'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalRelation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalRelation(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3d805c2a_4801_440e_9e4d_0fa5585c76ae',
    
    class_name='ElectrochemicalRelation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_3d805c2a_4801_440e_9e4d_0fa5585c76ae',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalRelation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    