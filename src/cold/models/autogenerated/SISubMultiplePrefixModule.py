
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIPrefixModule import SIPrefix







class SISubMultiplePrefix(SIPrefix):
    """
    Class representing the `SISubMultiplePrefix` entity, which inherits from:
    - SIPrefix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_48fc9480_78c3_4c81_a126_019df20d58d9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SISubMultiplePrefix'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SISubMultiplePrefix(
    
    class_iri='https://w3id.org/emmo#EMMO_48fc9480_78c3_4c81_a126_019df20d58d9',
    
    class_name='SISubMultiplePrefix',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_48fc9480_78c3_4c81_a126_019df20d58d9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SISubMultiplePrefix',
        alias="class_name"
    )
    

    
    

    

    