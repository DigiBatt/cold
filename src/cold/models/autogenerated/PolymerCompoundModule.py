
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OrganicCompoundModule import OrganicCompound







class PolymerCompound(OrganicCompound):
    """
    Class representing the `PolymerCompound` entity, which inherits from:
    - OrganicCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_7e716191_b301_4d63_bb6b_93323ffe51bf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PolymerCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PolymerCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_7e716191_b301_4d63_bb6b_93323ffe51bf',
    
    class_name='PolymerCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_7e716191_b301_4d63_bb6b_93323ffe51bf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PolymerCompound',
        alias="class_name"
    )
    

    
    

    

    