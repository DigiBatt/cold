
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SystemUnitModule import SystemUnit







class SIUnit(SystemUnit):
    """
    Class representing the `SIUnit` entity, which inherits from:
    - SystemUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_feb03a8a_bbb6_4918_a891_46713ef557f4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_feb03a8a_bbb6_4918_a891_46713ef557f4',
    
    class_name='SIUnit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_feb03a8a_bbb6_4918_a891_46713ef557f4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    