
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CastingModule import Casting







class ContinuousCasting(Casting):
    """
    Class representing the `ContinuousCasting` entity, which inherits from:
    - Casting

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_4b77c8ac_6d0e_456a_af41_ce43601b28b7'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ContinuousCasting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ContinuousCasting(
    
    class_iri='https://w3id.org/emmo#EMMO_4b77c8ac_6d0e_456a_af41_ce43601b28b7',
    
    class_name='ContinuousCasting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_4b77c8ac_6d0e_456a_af41_ce43601b28b7',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ContinuousCasting',
        alias="class_name"
    )
    

    
    

    

    