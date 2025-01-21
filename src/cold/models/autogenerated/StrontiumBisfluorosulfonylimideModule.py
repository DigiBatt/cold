
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumBisfluorosulfonylimide(StrontiumSaltCompound):
    """
    Class representing the `StrontiumBisfluorosulfonylimide` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_41cd4dfd_2288_48b2_a1e3_d13821c21a1e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumBisfluorosulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumBisfluorosulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_41cd4dfd_2288_48b2_a1e3_d13821c21a1e',
    
    class_name='StrontiumBisfluorosulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_41cd4dfd_2288_48b2_a1e3_d13821c21a1e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumBisfluorosulfonylimide',
        alias="class_name"
    )
    

    
    

    

    