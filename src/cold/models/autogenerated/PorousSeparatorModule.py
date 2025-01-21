
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SeparatorModule import Separator







class PorousSeparator(Separator):
    """
    Class representing the `PorousSeparator` entity, which inherits from:
    - Separator

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_58413d4e_2885_459e_ac06_8d45e661cf91'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PorousSeparator'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PorousSeparator(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_58413d4e_2885_459e_ac06_8d45e661cf91',
    
    class_name='PorousSeparator',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_58413d4e_2885_459e_ac06_8d45e661cf91',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PorousSeparator',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    