
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IntentionalProcessModule import IntentionalProcess







class TechnologyProcess(IntentionalProcess):
    """
    Class representing the `TechnologyProcess` entity, which inherits from:
    - IntentionalProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2b9cbfb5_dbd0_4a68_9c6f_acc41b40dd72'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TechnologyProcess'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TechnologyProcess(
    
    class_iri='https://w3id.org/emmo#EMMO_2b9cbfb5_dbd0_4a68_9c6f_acc41b40dd72',
    
    class_name='TechnologyProcess',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2b9cbfb5_dbd0_4a68_9c6f_acc41b40dd72',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TechnologyProcess',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    