
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntentionalProcessModule import IntentionalProcess



from .ElectrodeReactionModule import ElectrodeReaction







class Electrodeposition(IntentionalProcess, ElectrodeReaction):
    """
    Class representing the `Electrodeposition` entity, which inherits from:
    - IntentionalProcess, ElectrodeReaction

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f0c24970_4c14_4207_bd78_5f2181a67085'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electrodeposition'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Electrodeposition(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f0c24970_4c14_4207_bd78_5f2181a67085',
    
    class_name='Electrodeposition',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f0c24970_4c14_4207_bd78_5f2181a67085',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electrodeposition',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    