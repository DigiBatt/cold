
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromChipModule import FormingFromChip







class ChipboardManufacturing(FormingFromChip):
    """
    Class representing the `ChipboardManufacturing` entity, which inherits from:
    - FormingFromChip

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_375aaa5a_998f_4626_83e0_c7d7e52a6565'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChipboardManufacturing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChipboardManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_375aaa5a_998f_4626_83e0_c7d7e52a6565',
    
    class_name='ChipboardManufacturing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_375aaa5a_998f_4626_83e0_c7d7e52a6565',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChipboardManufacturing',
        alias="class_name"
    )
    

    
    

    

    