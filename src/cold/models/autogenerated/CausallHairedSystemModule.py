
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CausalSystemModule import CausalSystem







class CausallHairedSystem(CausalSystem):
    """
    Class representing the `CausallHairedSystem` entity, which inherits from:
    - CausalSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4bb03d40_78d2_45a4_9cb0_4336c9fc3b70'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CausallHairedSystem'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CausallHairedSystem(
    
    class_iri='https://w3id.org/emmo#EMMO_4bb03d40_78d2_45a4_9cb0_4336c9fc3b70',
    
    class_name='CausallHairedSystem',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4bb03d40_78d2_45a4_9cb0_4336c9fc3b70',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CausallHairedSystem',
        alias="class_name"
    )
    

    
    

    

    