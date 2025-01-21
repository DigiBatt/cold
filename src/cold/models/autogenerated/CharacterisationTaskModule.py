
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TaskModule import Task



from .CharacterisationProcedureModule import CharacterisationProcedure







class CharacterisationTask(Task, CharacterisationProcedure):
    """
    Class representing the `CharacterisationTask` entity, which inherits from:
    - Task, CharacterisationProcedure

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationTask'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CharacterisationTask'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CharacterisationTask(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationTask',
    
    class_name='CharacterisationTask',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#CharacterisationTask',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CharacterisationTask',
        alias="class_name"
    )
    

    
    

    

    