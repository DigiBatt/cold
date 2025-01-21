
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .BariumSaltCompoundModule import BariumSaltCompound







class BariumBistrifluoromethanesulfonylimide(BariumSaltCompound):
    """
    Class representing the `BariumBistrifluoromethanesulfonylimide` entity, which inherits from:
    - BariumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_05b11934_6a3e_4434_855b_111aced0a6be'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BariumBistrifluoromethanesulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BariumBistrifluoromethanesulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_05b11934_6a3e_4434_855b_111aced0a6be',
    
    class_name='BariumBistrifluoromethanesulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_05b11934_6a3e_4434_855b_111aced0a6be',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BariumBistrifluoromethanesulfonylimide',
        alias="class_name"
    )
    

    
    

    

    