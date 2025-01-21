
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ZincSaltCompoundModule import ZincSaltCompound







class ZincBistrifluoromethanesulfonylimide(ZincSaltCompound):
    """
    Class representing the `ZincBistrifluoromethanesulfonylimide` entity, which inherits from:
    - ZincSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_656bd621_963a_4ff0_b606_7e5a952bda3a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincBistrifluoromethanesulfonylimide'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincBistrifluoromethanesulfonylimide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_656bd621_963a_4ff0_b606_7e5a952bda3a',
    
    class_name='ZincBistrifluoromethanesulfonylimide',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_656bd621_963a_4ff0_b606_7e5a952bda3a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincBistrifluoromethanesulfonylimide',
        alias="class_name"
    )
    

    
    

    

    