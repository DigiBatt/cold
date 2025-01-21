
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .RoleModule import Role







class TemporalRole(Role):
    """
    Class representing the `TemporalRole` entity, which inherits from:
    - Role

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0e1f2009_bf12_49d1_99f3_1422e5287d82'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TemporalRole'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TemporalRole(
    
    class_iri='https://w3id.org/emmo#EMMO_0e1f2009_bf12_49d1_99f3_1422e5287d82',
    
    class_name='TemporalRole',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0e1f2009_bf12_49d1_99f3_1422e5287d82',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TemporalRole',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    