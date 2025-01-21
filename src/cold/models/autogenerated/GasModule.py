
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FluidModule import Fluid







class Gas(Fluid):
    """
    Class representing the `Gas` entity, which inherits from:
    - Fluid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_04f2a2d5_e799_4692_a654_420e76f5acc1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Gas'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Gas(
    
    class_iri='https://w3id.org/emmo#EMMO_04f2a2d5_e799_4692_a654_420e76f5acc1',
    
    class_name='Gas',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_04f2a2d5_e799_4692_a654_420e76f5acc1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Gas',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    