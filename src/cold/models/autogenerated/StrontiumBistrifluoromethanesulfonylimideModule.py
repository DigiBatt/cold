
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumBistrifluoromethanesulfonylimide(StrontiumSaltCompound):
    """
    Class representing the `StrontiumBistrifluoromethanesulfonylimide` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_d0e03160_256a_4cb2_a086_8f65d3abf62e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumBistrifluoromethanesulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumBistrifluoromethanesulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_d0e03160_256a_4cb2_a086_8f65d3abf62e',
    
    class_name='StrontiumBistrifluoromethanesulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_d0e03160_256a_4cb2_a086_8f65d3abf62e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumBistrifluoromethanesulfonylimide',
        alias="class_name"
    )
    

    
    

    

    