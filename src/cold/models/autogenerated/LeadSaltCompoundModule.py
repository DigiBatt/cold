
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalSaltCompoundModule import TransitionMetalSaltCompound







class LeadSaltCompound(TransitionMetalSaltCompound):
    """
    Class representing the `LeadSaltCompound` entity, which inherits from:
    - TransitionMetalSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0331ffd2_7cb2_40d3_80ce_8b4ab7b3adc5'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'LeadSaltCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = LeadSaltCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0331ffd2_7cb2_40d3_80ce_8b4ab7b3adc5',
    
    class_name='LeadSaltCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0331ffd2_7cb2_40d3_80ce_8b4ab7b3adc5',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'LeadSaltCompound',
        alias="class_name"
    )
    

    
    

    

    