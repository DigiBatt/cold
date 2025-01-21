
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemporalTileModule import TemporalTile



from .StepModule import Step







class SerialStep(TemporalTile, Step):
    """
    Class representing the `SerialStep` entity, which inherits from:
    - TemporalTile, Step

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2666a7e3_2ad4_49a0_899e_329607231f4b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SerialStep'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SerialStep(
    
    class_iri='https://w3id.org/emmo#EMMO_2666a7e3_2ad4_49a0_899e_329607231f4b',
    
    class_name='SerialStep',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2666a7e3_2ad4_49a0_899e_329607231f4b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SerialStep',
        alias="class_name"
    )
    

    
    

    

    