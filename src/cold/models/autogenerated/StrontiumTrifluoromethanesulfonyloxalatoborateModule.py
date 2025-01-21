
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .StrontiumSaltCompoundModule import StrontiumSaltCompound







class StrontiumTrifluoromethanesulfonyloxalatoborate(StrontiumSaltCompound):
    """
    Class representing the `StrontiumTrifluoromethanesulfonyloxalatoborate` entity, which inherits from:
    - StrontiumSaltCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_ab3606c2_a1e3_4e40_b427_766c586b5f77'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StrontiumTrifluoromethanesulfonyloxalatoborate'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StrontiumTrifluoromethanesulfonyloxalatoborate(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_ab3606c2_a1e3_4e40_b427_766c586b5f77',
    
    class_name='StrontiumTrifluoromethanesulfonyloxalatoborate',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_ab3606c2_a1e3_4e40_b427_766c586b5f77',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StrontiumTrifluoromethanesulfonyloxalatoborate',
        alias="class_name"
    )
    

    
    

    

    