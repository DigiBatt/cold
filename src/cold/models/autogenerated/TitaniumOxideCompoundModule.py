
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TransitionMetalOxideCompoundModule import TransitionMetalOxideCompound







class TitaniumOxideCompound(TransitionMetalOxideCompound):
    """
    Class representing the `TitaniumOxideCompound` entity, which inherits from:
    - TransitionMetalOxideCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_001ca83b_5372_4d77_a836_4d48074b7e63'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TitaniumOxideCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TitaniumOxideCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_001ca83b_5372_4d77_a836_4d48074b7e63',
    
    class_name='TitaniumOxideCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_001ca83b_5372_4d77_a836_4d48074b7e63',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TitaniumOxideCompound',
        alias="class_name"
    )
    

    
    

    

    