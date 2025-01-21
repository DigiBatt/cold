
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TemporalRoleModule import TemporalRole



from .ObjectModule import Object







class SubObject(TemporalRole, Object):
    """
    Class representing the `SubObject` entity, which inherits from:
    - TemporalRole, Object

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2553c342_fc28_47d8_8e19_7a98fa08f150'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SubObject'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SubObject(
    
    class_iri='https://w3id.org/emmo#EMMO_2553c342_fc28_47d8_8e19_7a98fa08f150',
    
    class_name='SubObject',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2553c342_fc28_47d8_8e19_7a98fa08f150',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SubObject',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    