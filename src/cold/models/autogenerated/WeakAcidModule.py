
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AcidModule import Acid







class WeakAcid(Acid):
    """
    Class representing the `WeakAcid` entity, which inherits from:
    - Acid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_29fd347b_6a15_4c98_a982_84cf555b0b86'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'WeakAcid'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = WeakAcid(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_29fd347b_6a15_4c98_a982_84cf555b0b86',
    
    class_name='WeakAcid',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_29fd347b_6a15_4c98_a982_84cf555b0b86',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'WeakAcid',
        alias="class_name"
    )
    

    
    

    

    