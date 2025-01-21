
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CuttingModule import Cutting







class ShearCutting(Cutting):
    """
    Class representing the `ShearCutting` entity, which inherits from:
    - Cutting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_1d6b63d5_9938_483c_ad62_a09ac34153c9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ShearCutting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ShearCutting(
    
    class_iri='https://w3id.org/emmo#EMMO_1d6b63d5_9938_483c_ad62_a09ac34153c9',
    
    class_name='ShearCutting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_1d6b63d5_9938_483c_ad62_a09ac34153c9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ShearCutting',
        alias="class_name"
    )
    

    
    

    

    