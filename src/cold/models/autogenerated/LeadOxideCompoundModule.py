
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class LeadOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `LeadOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_bc9ba950_96c1_4ac2_a0e2_1c4f7f001b1d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LeadOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LeadOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_bc9ba950_96c1_4ac2_a0e2_1c4f7f001b1d',
    
    class_name='LeadOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_bc9ba950_96c1_4ac2_a0e2_1c4f7f001b1d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LeadOxideCompound',
        alias="class_name"
    )
    

    
    

    

    