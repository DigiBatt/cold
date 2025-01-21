
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RedAntiQuarkModule import RedAntiQuark



from .StrangeAntiQuarkModule import StrangeAntiQuark







class RedStrangeAntiQuark(RedAntiQuark, StrangeAntiQuark):
    """
    Class representing the `RedStrangeAntiQuark` entity, which inherits from:
    - RedAntiQuark, StrangeAntiQuark

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_73aa05b8_51be_4863_bb0b_35845ac9362b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RedStrangeAntiQuark'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RedStrangeAntiQuark(
    
    class_iri='https://w3id.org/emmo#EMMO_73aa05b8_51be_4863_bb0b_35845ac9362b',
    
    class_name='RedStrangeAntiQuark',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_73aa05b8_51be_4863_bb0b_35845ac9362b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RedStrangeAntiQuark',
        alias="class_name"
    )
    

    
    

    

    