
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CastingModule import Casting







class DieCasting(Casting):
    """
    Class representing the `DieCasting` entity, which inherits from:
    - Casting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a85d0b8a_588e_423f_b799_97b0890e9183'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DieCasting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DieCasting(
    
    class_iri='https://w3id.org/emmo#EMMO_a85d0b8a_588e_423f_b799_97b0890e9183',
    
    class_name='DieCasting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a85d0b8a_588e_423f_b799_97b0890e9183',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DieCasting',
        alias="class_name"
    )
    

    
    

    

    